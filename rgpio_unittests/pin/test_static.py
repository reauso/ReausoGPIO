"""Tests for static pin types."""

from abc import ABC
from dataclasses import FrozenInstanceError
from unittest import TestCase

from rgpio.pin.configurable import ConfigurablePin
from rgpio.pin.pin import Pin
from rgpio.pin.static import (
    GroundPin,
    NoConnectionPin,
    PowerPin,
    ReferencePin,
    ResetPin,
    StaticPin,
)


class TestStaticPinAbstractBase(TestCase):
    """Tests for the StaticPin abstract base class."""

    def test_StaticPin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(StaticPin, Pin))

    def test_StaticPin__InheritsFromABC__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(StaticPin, ABC))

    def test_StaticPin__IsNotSubclassOfConfigurablePin__ReturnsFalse(self) -> None:
        # Arrange & Act & Assert
        self.assertFalse(issubclass(StaticPin, ConfigurablePin))


class TestPowerPin(TestCase):
    """Tests for the PowerPin frozen dataclass."""

    def test_PowerPin__Creation__StoresVoltage(self) -> None:
        # Arrange & Act
        pin = PowerPin(voltage=3.3)

        # Assert
        self.assertEqual(pin.voltage, 3.3)

    def test_PowerPin__IsSubclassOfStaticPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(PowerPin, StaticPin))

    def test_PowerPin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(PowerPin, Pin))

    def test_PowerPin__IsNotSubclassOfConfigurablePin__ReturnsFalse(self) -> None:
        # Arrange & Act & Assert
        self.assertFalse(issubclass(PowerPin, ConfigurablePin))

    def test_PowerPin__IsFrozen__RaisesOnAssignment(self) -> None:
        # Arrange
        pin = PowerPin(voltage=5.0)

        # Act & Assert
        with self.assertRaises(FrozenInstanceError):
            pin.voltage = 3.3  # type: ignore[misc]

    def test_PowerPin__Equality__SameVoltagePinsAreEqual(self) -> None:
        # Arrange
        pin1 = PowerPin(voltage=3.3)
        pin2 = PowerPin(voltage=3.3)

        # Act & Assert
        self.assertEqual(pin1, pin2)

    def test_PowerPin__Equality__DifferentVoltagePinsAreNotEqual(self) -> None:
        # Arrange
        pin1 = PowerPin(voltage=3.3)
        pin2 = PowerPin(voltage=5.0)

        # Act & Assert
        self.assertNotEqual(pin1, pin2)

    def test_PowerPin__KeywordOnly__PositionalArgRaises(self) -> None:
        # Act & Assert
        with self.assertRaises(TypeError):
            PowerPin(3.3)  # type: ignore[misc]

    def test_PowerPin__NegativeVoltage__CreatesSuccessfully(self) -> None:
        # Arrange & Act
        pin = PowerPin(voltage=-5.0)

        # Assert
        self.assertEqual(pin.voltage, -5.0)


class TestGroundPin(TestCase):
    """Tests for the GroundPin frozen dataclass."""

    def test_GroundPin__Creation__Succeeds(self) -> None:
        # Arrange & Act
        pin = GroundPin()

        # Assert
        self.assertIsInstance(pin, GroundPin)

    def test_GroundPin__IsSubclassOfStaticPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(GroundPin, StaticPin))

    def test_GroundPin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(GroundPin, Pin))

    def test_GroundPin__Equality__AllInstancesAreEqual(self) -> None:
        # Arrange
        pin1 = GroundPin()
        pin2 = GroundPin()

        # Act & Assert
        self.assertEqual(pin1, pin2)


class TestResetPin(TestCase):
    """Tests for the ResetPin frozen dataclass."""

    def test_ResetPin__Creation__Succeeds(self) -> None:
        # Arrange & Act
        pin = ResetPin()

        # Assert
        self.assertIsInstance(pin, ResetPin)

    def test_ResetPin__IsSubclassOfStaticPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(ResetPin, StaticPin))

    def test_ResetPin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(ResetPin, Pin))

    def test_ResetPin__Equality__AllInstancesAreEqual(self) -> None:
        # Arrange
        pin1 = ResetPin()
        pin2 = ResetPin()

        # Act & Assert
        self.assertEqual(pin1, pin2)


class TestReferencePin(TestCase):
    """Tests for the ReferencePin frozen dataclass."""

    def test_ReferencePin__Creation__StoresVoltage(self) -> None:
        # Arrange & Act
        pin = ReferencePin(voltage=1.1)

        # Assert
        self.assertEqual(pin.voltage, 1.1)

    def test_ReferencePin__IsSubclassOfStaticPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(ReferencePin, StaticPin))

    def test_ReferencePin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(ReferencePin, Pin))

    def test_ReferencePin__IsFrozen__RaisesOnAssignment(self) -> None:
        # Arrange
        pin = ReferencePin(voltage=1.1)

        # Act & Assert
        with self.assertRaises(FrozenInstanceError):
            pin.voltage = 2.5  # type: ignore[misc]

    def test_ReferencePin__Equality__SameVoltagePinsAreEqual(self) -> None:
        # Arrange
        pin1 = ReferencePin(voltage=1.1)
        pin2 = ReferencePin(voltage=1.1)

        # Act & Assert
        self.assertEqual(pin1, pin2)


class TestNoConnectionPin(TestCase):
    """Tests for the NoConnectionPin frozen dataclass."""

    def test_NoConnectionPin__Creation__Succeeds(self) -> None:
        # Arrange & Act
        pin = NoConnectionPin()

        # Assert
        self.assertIsInstance(pin, NoConnectionPin)

    def test_NoConnectionPin__IsSubclassOfStaticPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(NoConnectionPin, StaticPin))

    def test_NoConnectionPin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(NoConnectionPin, Pin))

    def test_NoConnectionPin__Equality__AllInstancesAreEqual(self) -> None:
        # Arrange
        pin1 = NoConnectionPin()
        pin2 = NoConnectionPin()

        # Act & Assert
        self.assertEqual(pin1, pin2)
