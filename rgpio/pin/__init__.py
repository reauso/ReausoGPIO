"""Pin model: modes, capabilities, and pin types."""

from rgpio.pin.configurable import ConfigurablePin, GpioPin
from rgpio.pin.mode import Modes, PinMode
from rgpio.pin.pin import Pin
from rgpio.pin.static import (
    GroundPin,
    NoConnectionPin,
    PowerPin,
    ReferencePin,
    ResetPin,
    StaticPin,
)


class Pins:
    """Namespace providing access to all standard pin types.

    Usage::

        from rgpio import Pins

        power = Pins.Power(voltage=3.3)
        ground = Pins.Ground()
        gpio = Pins.Gpio(capabilities=frozenset({Modes.DigitalInput.PullUp}))
    """

    Power = PowerPin
    Ground = GroundPin
    Reset = ResetPin
    Reference = ReferencePin
    NoConnection = NoConnectionPin
    Gpio = GpioPin


__all__ = [
    "ConfigurablePin",
    "GpioPin",
    "GroundPin",
    "Modes",
    "NoConnectionPin",
    "Pin",
    "PinMode",
    "Pins",
    "PowerPin",
    "ReferencePin",
    "ResetPin",
    "StaticPin",
]
