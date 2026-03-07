"""Abstract base class for all pin types."""

from __future__ import annotations

from abc import ABC


class Pin(ABC):
    """Abstract base for all pin types.

    Pins describe the electrical characteristics of a physical pin.
    They carry no numeric identifier; all identification and numbering
    is handled at the board level.

    The pin hierarchy has two intermediate categories:

    - ``StaticPin`` — Fixed purpose, no user configuration.
    - ``ConfigurablePin`` — User-configurable, has capabilities and mode.

    The hierarchy is extensible — subclass the appropriate abstract base
    to create custom pin types for hardware not covered by the standard set.
    """


__all__ = [
    "Pin",
]
