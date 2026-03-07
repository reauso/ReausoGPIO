"""Static pin types with fixed, unchanging purposes."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from rgpio.pin.pin import Pin


class StaticPin(Pin, ABC):
    """Abstract base for pins with a fixed purpose.

    Static pins represent hardware connections that are not user-configurable.
    They exist for accurate circuit modeling but have no capabilities or mode.
    """


@dataclass(frozen=True, kw_only=True)
class PowerPin(StaticPin):
    """Fixed voltage output pin (e.g. 3.3V, 5V).

    Attributes:
        voltage: Output voltage in volts.
    """

    voltage: float


@dataclass(frozen=True, kw_only=True)
class GroundPin(StaticPin):
    """Electrical ground reference pin."""


@dataclass(frozen=True, kw_only=True)
class ResetPin(StaticPin):
    """Board reset pin."""


@dataclass(frozen=True, kw_only=True)
class ReferencePin(StaticPin):
    """Voltage reference pin (e.g. analog reference).

    Attributes:
        voltage: Reference voltage in volts.
    """

    voltage: float


@dataclass(frozen=True, kw_only=True)
class NoConnectionPin(StaticPin):
    """Pin that is physically present but not connected."""


__all__ = [
    "GroundPin",
    "NoConnectionPin",
    "PowerPin",
    "ReferencePin",
    "ResetPin",
    "StaticPin",
]
