"""Tests for the Pin abstract base class and Pins namespace."""

from abc import ABC
from unittest import TestCase

from rgpio.pin.configurable import ConfigurablePin, GpioPin
from rgpio.pin.pin import Pin
from rgpio.pin.static import (
    GroundPin,
    NoConnectionPin,
    PowerPin,
    ReferencePin,
    ResetPin,
    StaticPin,
)

from rgpio.pin import Pins


class TestPinAbstractBase(TestCase):
    """Tests for the Pin abstract base class."""

    def test_Pin__InheritsFromABC__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(Pin, ABC))

    def test_Pin__CustomSubclass__IsSubclassOfPin(self) -> None:
        # Arrange
        class CustomPin(Pin):
            pass

        # Act & Assert
        self.assertTrue(issubclass(CustomPin, Pin))
        self.assertIsInstance(CustomPin(), Pin)


class TestPinsNamespace(TestCase):
    """Tests for the Pins namespace container class."""

    def test_Pins__PowerAttribute__IsPowerPinClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Pins.Power, PowerPin)

    def test_Pins__GroundAttribute__IsGroundPinClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Pins.Ground, GroundPin)

    def test_Pins__ResetAttribute__IsResetPinClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Pins.Reset, ResetPin)

    def test_Pins__ReferenceAttribute__IsReferencePinClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Pins.Reference, ReferencePin)

    def test_Pins__NoConnectionAttribute__IsNoConnectionPinClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Pins.NoConnection, NoConnectionPin)

    def test_Pins__GpioAttribute__IsGpioPinClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Pins.Gpio, GpioPin)
