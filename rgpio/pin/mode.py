"""Pin modes defining the capabilities and configurations of GPIO pins."""

from __future__ import annotations


class PinMode:
    """Base class for all pin modes.

    Modes serve dual purpose:
    - As types in a capabilities frozenset (what a pin CAN do)
    - As base classes for configuring pins (what a pin IS doing)

    Subclasses are automatically registered as attributes on their
    parent mode class, enabling namespace access patterns like
    ``DigitalInput.PullUp``.

    To opt out of auto-registration, pass ``register=False``::

        class InternalMode(DigitalInput, register=False):
            pass
    """

    def __init_subclass__(cls, register: bool = True, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        if not register:
            return
        for base in cls.__bases__:
            if base is not PinMode and issubclass(base, PinMode):
                setattr(base, cls.__name__, cls)

    def __eq__(self, other: object) -> bool:
        return type(self) is type(other)

    def __hash__(self) -> int:
        return hash(type(self))


# --- Digital modes ---


class DigitalInput(PinMode):
    """Digital input mode."""


class PullUp(DigitalInput):
    """Digital input with internal pull-up resistor enabled."""


class PullDown(DigitalInput):
    """Digital input with internal pull-down resistor enabled."""


class Floating(DigitalInput):
    """Digital input in high-impedance (floating) state."""


class DigitalOutput(PinMode):
    """Digital output mode."""


class PushPull(DigitalOutput):
    """Digital output in push-pull drive configuration."""


class OpenDrain(DigitalOutput):
    """Digital output in open-drain configuration."""


# --- Analog modes ---


class AnalogInput(PinMode):
    """Analog input mode (ADC)."""


class AnalogOutput(PinMode):
    """Analog output mode (DAC)."""


# --- PWM ---


class PWM(PinMode):
    """Pulse-width modulation output mode."""


# --- Communication protocols ---


class I2C(PinMode):
    """I2C communication mode."""


class SDA(I2C):
    """I2C serial data line."""


class SCL(I2C):
    """I2C serial clock line."""


class SPI(PinMode):
    """SPI communication mode."""


class MOSI(SPI):
    """SPI master-out slave-in data line."""


class MISO(SPI):
    """SPI master-in slave-out data line."""


class CLK(SPI):
    """SPI clock line."""


class CS(SPI):
    """SPI chip select line."""


class UART(PinMode):
    """UART communication mode."""


class TX(UART):
    """UART transmit line."""


class RX(UART):
    """UART receive line."""


# --- Mode namespace ---


class Modes:
    """Namespace providing access to all standard pin modes.

    Usage::

        from rgpio import Modes

        caps = frozenset({Modes.DigitalInput.PullUp, Modes.PWM})
    """

    DigitalInput = DigitalInput
    DigitalOutput = DigitalOutput
    AnalogInput = AnalogInput
    AnalogOutput = AnalogOutput
    PWM = PWM
    I2C = I2C
    SPI = SPI
    UART = UART


__all__ = [
    "Modes",
    "PinMode",
]
