# ReausoGPIO - Idea

## Vision

ReausoGPIO is a unified adapter layer for GPIO libraries that models real-world circuits in software. Instead of coding directly against a specific GPIO library, users describe their physical setup - boards, components, and how they are wired together - and the library translates high-level component operations into the correct low-level GPIO calls for whichever underlying library is in use.

## Architecture Layers

```
User Code  ->  Components  ->  Board / Pins  ->  GPIO Interface  ->  GPIO Library  ->  Hardware
             \____________/   \______________________________________________/
              Higher Layer                    Core System
```

The user interacts with components. Components are attached to a board's pins. The board delegates pin operations through a GPIO interface to the actual library that controls the hardware.

## Performance

Performance is a core requirement. The adapter layer must add minimal overhead when forwarding pin operations to the underlying GPIO library. This is achieved through the two-phase build model: all validation, resolution, and wiring happens once at build time, so the runtime path is a thin, direct forwarding layer with no unnecessary work.

## Two-Phase Build Model

The library uses a two-phase approach that separates circuit design from execution.

### Phase 1: Blueprint (Mutable)

The user builds their circuit declaratively: add boards, configure pins, attach components, define connections, register event handlers. Everything is mutable and nothing is validated yet. The blueprint describes *what* the circuit looks like.

### Phase 2: Build (Blueprint -> Runtime)

Calling `build()` on a blueprint:
1. Validates all connections, pin compatibility, and capability requirements
2. Resolves signal chains (accounting for components like relays that transform signals)
3. Caches direct function references to the underlying GPIO library for fast forwarding
4. Pre-computes all pin mappings and forwarding paths
5. Wires event handlers into the runtime event system
6. Produces a frozen, immutable runtime

**Build options** control what the runtime includes. For example, building with debug support adds signal tracing (e.g. voltage tracking across components). Without debug, these paths are omitted entirely for maximum speed.

The blueprint is reusable — it can be built multiple times with different options (e.g. once with debug, once without).

### Runtime (Frozen Structure, Mutable State)

The built runtime has two aspects:
- **Structure is frozen** — The circuit topology (what's connected to what, forwarding chains, resolved references) is immutable. You cannot rewire at runtime.
- **State is mutable** — Pin values (high/low), PWM duty cycles, analog readings change with every operation. State is read/written through the pre-resolved, fast forwarding paths.

This separation means the runtime can trust its structure completely and skip all validation on every operation.

### Lifecycle

The runtime acts as a context manager to guarantee cleanup of hardware resources. When the context exits (normally or due to an exception), all pins are reset to a safe state and resources are released.

## Core System

The foundational layer that everything else builds on. Implementation order: Pins -> GPIO Interface -> Board.

### Pins

The most fundamental building block. A pin represents a physical pin on a board. All pin types are modeled — not just GPIO pins, but also power, ground, and other pins — to accurately represent real-world circuits.

#### Pin Hierarchy

Pins are organized into a class hierarchy with two intermediate categories:

```
Pin (abstract base)
├── StaticPin (abstract base) — Fixed purpose, no user configuration
│   ├── PowerPin              — Fixed voltage output (3.3V, 5V, etc.)
│   ├── GroundPin             — Electrical ground reference
│   ├── ResetPin              — Board reset
│   ├── ReferencePin          — Voltage reference (e.g. analog reference)
│   └── NoConnectionPin       — Physically present but not connected
└── ConfigurablePin (abstract base) — User-configurable, has capabilities and mode
    └── GpioPin               — General-purpose I/O with selectable capabilities
```

- **StaticPin** subclasses represent pins with a fixed, unchanging purpose. They exist for circuit modeling but are not configurable.
- **ConfigurablePin** subclasses represent pins that the user configures during the blueprint phase. They carry capabilities (what the pin CAN do) and a mode (what it's CONFIGURED to do).

The hierarchy is extensible — users can subclass the abstract bases to create custom pin types for hardware not covered by the standard set.

#### Capabilities and Mode

Each configurable pin has a set of **capabilities** describing what the hardware supports, and a **mode** selected by the user during the blueprint phase. The mode must be one of the pin's capabilities and is validated at build time.

Capabilities are role-specific — for example, I2C distinguishes between SDA and SCL roles because they serve different functions. The same applies to SPI (MOSI, MISO, CLK, CS) and UART (TX, RX).

**Standard capabilities** provided by the library:
- Digital input, digital output
- PWM
- Analog input, analog output
- I2C SDA, I2C SCL
- SPI MOSI, SPI MISO, SPI CLK, SPI CS
- UART TX, UART RX

**Capabilities are extensible** — users can define their own custom capabilities for protocols or hardware not anticipated by the library. Custom capabilities integrate seamlessly with configurable pins and the build process, just like the standard ones.

### GPIO Interface (Adapter)

The adapter layer between the board model and the actual hardware-controlling GPIO library. Uses a hybrid design:

- **ABC base** — A minimal abstract base class for lifecycle operations (setup, cleanup, pin configuration). Every adapter must implement this.
- **Protocol-based capabilities** — Separate capability interfaces for each capability group (`DigitalIO`, `PWMCapable`, `AnalogCapable`, `I2CCapable`, `SPICapable`, `UARTCapable`). An adapter implements only the capabilities its underlying library actually supports.
- **Build-time capability checking** — The build step checks which capabilities an adapter supports and gives clear errors if the circuit requires an unsupported operation.

This design follows the Interface Segregation Principle: an RPi.GPIO adapter implements `DigitalIO` + `PWMCapable` but not `I2CCapable`, while a pigpio adapter can implement all of them. Swapping the underlying library requires only changing the adapter implementation.

**Statefulness is not dictated by the library.** Each adapter implementation decides whether to track pin states internally based on its needs. A mock/emulation adapter is naturally stateful (it simulates the hardware). A real hardware adapter may be stateless and delegate state to the underlying library.

A **mock/stub GPIO interface** is included in the core for testing and development without hardware.

### Board

A board defines the physical pin layout of a microcontroller or single-board computer (Arduino, Raspberry Pi, ESP32, etc.). It declares all of its available pins — power, ground, GPIO, and other types — with their types and capabilities.

**Board definition and adapter are separate concerns:**
- A **board definition** describes hardware layout — "a Raspberry Pi 4 has 40 pins with these types and capabilities."
- An **adapter** handles GPIO library translation — "I use pigpio to control pins."
- The **blueprint** brings them together — the user associates a board with an adapter.
- The **build step** validates that the adapter supports all capabilities required by the board's configured pins.

This separation is important because the same board can use different GPIO libraries (RPi 4 with RPi.GPIO vs pigpio), and the same adapter can serve different board models.

The library ships common board definitions in separate platform packages. Users can also define their own boards for custom hardware.

## Package Ecosystem

The library is split into a lean core and separate platform packages:

- **`rgpio`** (core) — Pin model, board and adapter base classes, blueprint and build system, mock adapter. No hardware-specific code.
- **`rgpio-raspberry`** — Raspberry Pi board definitions and RPi-specific adapters (RPi.GPIO, pigpio, gpiozero). Specific adapters installable via optional dependency extras.
- **`rgpio-arduino`** — Arduino board definitions and Arduino adapters.
- **Additional platform packages** as needed (ESP32, BeagleBone, etc.).

This keeps the core dependency-free and lets users install only what they need for their hardware.

## Events

The library supports events at two levels:

- **Pin-level events** — Raw edge/level triggers on pins (rising edge, falling edge, level change).
- **Component-level events** — Semantic events on components (button pressed, sensor threshold reached).

Event handlers are registered during the blueprint phase only. During build, they are validated and wired into the runtime event system. At runtime, events fire through the pre-built paths. If dynamic behavior is needed, the registered callback itself contains the deciding logic.

## Error Handling

The library throws exceptions for errors (hardware failures, communication timeouts, etc.). It is the user's responsibility to catch and handle them. No internal error handling complexity is added. This may be revisited if the library introduces its own threads in the future.

## Concurrency

Thread safety for bus-level access (I2C, SPI) is the responsibility of the underlying GPIO library, not this adapter layer. ReausoGPIO is a thin forwarding layer and does not add its own locking or synchronization.

## Higher Layer (Future)

Built on top of the core system. Not part of the initial implementation scope.

### Components

Digital representations of physical parts such as LEDs, pumps, relays, buttons, and sensors. Each component knows what it needs electrically (e.g. a digital output pin, a PWM pin) and exposes a meaningful API (e.g. `led.on()`, `pump.start()`). Components can be connected to each other and to boards, reflecting the actual circuit. Components like relays can transform signals, which is resolved during the build phase.

### Connections

The wiring between components and boards. Connections mirror the physical circuit: a component is connected to specific pins on a board, and components can be connected to each other (e.g. a relay controlling a pump). This makes the software model a direct reflection of the real-world setup.

### Factories and Facades

Convenience layer for common workflows:

- **Factories** handle the creation of boards, adapters, components, and other objects. They encapsulate creation complexity and can select the right concrete types based on parameters or installed packages.
- **Facades** simplify common setups — for example, auto-detecting the current board, picking a default adapter, and wiring everything up in a single call.

## Open Design Questions

*To be discussed and expanded in future sessions.*
