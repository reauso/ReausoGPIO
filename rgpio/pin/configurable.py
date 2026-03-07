"""Configurable pin types with user-selectable capabilities and modes."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from rgpio.pin.mode import PinMode
from rgpio.pin.pin import Pin


class ConfigurablePin(Pin, ABC):
    """Abstract base for user-configurable pins.

    Configurable pins carry capabilities (what the pin CAN do) and a mode
    (what it's CONFIGURED to do). The mode is set during the blueprint phase
    and validated against capabilities at build time.

    Setting a mode implicitly selects the active capability — the active
    capability is derived from ``type(self.mode)``.

    Subclasses must provide:
        capabilities: frozenset[type[PinMode]] — the set of mode types
            this pin supports.
        mode: PinMode | None — the currently configured mode, or None
            if unconfigured.
    """


@dataclass(frozen=True, kw_only=True)
class GpioPin(ConfigurablePin):
    """General-purpose I/O pin with selectable capabilities.

    Attributes:
        capabilities: Frozenset of PinMode types this pin supports.
        mode: The currently configured mode instance, or None if unconfigured.
    """

    capabilities: frozenset[type[PinMode]]
    mode: PinMode | None = None


__all__ = [
    "ConfigurablePin",
    "GpioPin",
]
