# ReausoGPIO - Idea

## Vision

ReausoGPIO is a unified adapter layer for GPIO libraries that models real-world circuits in software. Instead of coding directly against a specific GPIO library, users describe their physical setup - boards, components, and how they are wired together - and the library translates high-level component operations into the correct low-level GPIO calls for whichever underlying library is in use.

## Core Concepts

### Components

Digital representations of physical parts such as LEDs, pumps, relays, buttons, and sensors. Each component knows what it needs electrically (e.g. a digital output pin, a PWM pin) and exposes a meaningful API (e.g. `led.on()`, `pump.start()`). Components can be connected to each other and to boards, reflecting the actual circuit.

### Boards

Models of microcontrollers and single-board computers like Arduino, Raspberry Pi, or ESP32. A board defines all of its available pins with their types and capabilities (digital I/O, analog, PWM, I2C, SPI, etc.). The digital board is the central hub that components attach to.

### Connections

The wiring between components and boards. Connections mirror the physical circuit: a component is connected to specific pins on a board, and components can be connected to each other (e.g. a relay controlling a pump). This makes the software model a direct reflection of the real-world setup.

### GPIO Interface

The adapter layer between the board model and the actual hardware-controlling GPIO library. The board issues abstract pin operations (set high, read value, configure PWM) and the GPIO interface translates these into calls to the specific underlying library (RPi.GPIO, gpiozero, pigpio, Arduino firmware, etc.). Swapping the underlying library requires only changing the interface implementation, not the component or board code.

## Architecture Layers

```
User Code  ->  Components  ->  Board / Pins  ->  GPIO Interface  ->  GPIO Library  ->  Hardware
```

The user interacts with components. Components are attached to a board's pins. The board delegates pin operations through a GPIO interface to the actual library that controls the hardware.

## Open Design Questions

*To be discussed and expanded in future sessions.*
