"""Tests for configurable pin types."""

from abc import ABC
from dataclasses import FrozenInstanceError, replace
from unittest import TestCase

from rgpio.pin.configurable import ConfigurablePin, GpioPin
from rgpio.pin.mode import (
    AnalogOutput,
    DigitalInput,
    PWM,
    PinMode,
    PullUp,
)
from rgpio.pin.pin import Pin
from rgpio.pin.static import StaticPin


class TestConfigurablePinAbstractBase(TestCase):
    """Tests for the ConfigurablePin abstract base class."""

    def test_ConfigurablePin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(ConfigurablePin, Pin))

    def test_ConfigurablePin__InheritsFromABC__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(ConfigurablePin, ABC))

    def test_ConfigurablePin__IsNotSubclassOfStaticPin__ReturnsFalse(self) -> None:
        # Arrange & Act & Assert
        self.assertFalse(issubclass(ConfigurablePin, StaticPin))


class TestGpioPin(TestCase):
    """Tests for the GpioPin frozen dataclass."""

    def test_GpioPin__Creation__StoresCapabilitiesAndMode(self) -> None:
        # Arrange
        caps = frozenset({PullUp, PWM})
        mode = PullUp()

        # Act
        pin = GpioPin(capabilities=caps, mode=mode)

        # Assert
        self.assertEqual(pin.capabilities, caps)
        self.assertIsInstance(pin.mode, PullUp)

    def test_GpioPin__DefaultMode__IsNone(self) -> None:
        # Arrange & Act
        pin = GpioPin(capabilities=frozenset({PWM}))

        # Assert
        self.assertIsNone(pin.mode)

    def test_GpioPin__IsSubclassOfConfigurablePin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(GpioPin, ConfigurablePin))

    def test_GpioPin__IsSubclassOfPin__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(GpioPin, Pin))

    def test_GpioPin__IsNotSubclassOfStaticPin__ReturnsFalse(self) -> None:
        # Arrange & Act & Assert
        self.assertFalse(issubclass(GpioPin, StaticPin))

    def test_GpioPin__IsFrozen__RaisesOnModeAssignment(self) -> None:
        # Arrange
        pin = GpioPin(capabilities=frozenset({PWM}))

        # Act & Assert
        with self.assertRaises(FrozenInstanceError):
            pin.mode = PWM()  # type: ignore[misc]

    def test_GpioPin__IsFrozen__RaisesOnCapabilitiesAssignment(self) -> None:
        # Arrange
        pin = GpioPin(capabilities=frozenset({PWM}))

        # Act & Assert
        with self.assertRaises(FrozenInstanceError):
            pin.capabilities = frozenset()  # type: ignore[misc]

    def test_GpioPin__KeywordOnly__PositionalArgRaises(self) -> None:
        # Act & Assert
        with self.assertRaises(TypeError):
            GpioPin(frozenset({PWM}))  # type: ignore[misc]

    def test_GpioPin__Equality__SameCapsAndModePinsAreEqual(self) -> None:
        # Arrange
        caps = frozenset({PullUp, PWM})
        pin1 = GpioPin(capabilities=caps, mode=PullUp())
        pin2 = GpioPin(capabilities=caps, mode=PullUp())

        # Act & Assert
        self.assertEqual(pin1, pin2)

    def test_GpioPin__Equality__DifferentModePinsAreNotEqual(self) -> None:
        # Arrange
        caps = frozenset({PullUp, PWM})
        pin1 = GpioPin(capabilities=caps, mode=PullUp())
        pin2 = GpioPin(capabilities=caps, mode=PWM())

        # Act & Assert
        self.assertNotEqual(pin1, pin2)

    def test_GpioPin__Equality__DifferentCapsPinsAreNotEqual(self) -> None:
        # Arrange
        pin1 = GpioPin(capabilities=frozenset({PullUp, PWM}))
        pin2 = GpioPin(capabilities=frozenset({PWM}))

        # Act & Assert
        self.assertNotEqual(pin1, pin2)


class TestGpioPinModeCapability(TestCase):
    """Tests for deriving active capability from mode type."""

    def test_ModeType__WithMode__DerivesActiveCapability(self) -> None:
        # Arrange
        pin = GpioPin(
            capabilities=frozenset({PullUp, PWM}),
            mode=PullUp(),
        )

        # Act
        active_capability = type(pin.mode)

        # Assert
        self.assertIs(active_capability, PullUp)
        self.assertIn(active_capability, pin.capabilities)

    def test_ModeType__WithNoneMode__TypeIsNoneType(self) -> None:
        # Arrange
        pin = GpioPin(capabilities=frozenset({PWM}))

        # Act & Assert
        self.assertIsNone(pin.mode)


class TestGpioPinNoValidation(TestCase):
    """Tests verifying pins do NOT validate mode against capabilities.

    Validation is the build system's responsibility, not the pin's.
    """

    def test_NoValidation__ModeNotInCapabilities__CreatesSuccessfully(self) -> None:
        # Arrange & Act
        pin = GpioPin(
            capabilities=frozenset({PWM}),
            mode=PullUp(),
        )

        # Assert
        self.assertIsNotNone(pin.mode)

    def test_NoValidation__EmptyCapabilities__CreatesSuccessfully(self) -> None:
        # Arrange & Act
        pin = GpioPin(capabilities=frozenset())

        # Assert
        self.assertEqual(len(pin.capabilities), 0)


class TestGpioPinReplace(TestCase):
    """Tests for functional updates via dataclasses.replace."""

    def test_Replace__SetMode__ReturnsNewPinWithMode(self) -> None:
        # Arrange
        pin = GpioPin(capabilities=frozenset({PWM, PullUp}))

        # Act
        updated = replace(pin, mode=PWM())

        # Assert
        self.assertIsNone(pin.mode)
        self.assertIsInstance(updated.mode, PWM)
        self.assertIsNot(pin, updated)

    def test_Replace__ChangeMode__PreservesCapabilities(self) -> None:
        # Arrange
        caps = frozenset({PWM, PullUp})
        pin = GpioPin(capabilities=caps, mode=PullUp())

        # Act
        updated = replace(pin, mode=PWM())

        # Assert
        self.assertEqual(updated.capabilities, caps)


class TestGpioPinExtensibility(TestCase):
    """Tests for custom subclasses of ConfigurablePin."""

    def test_CustomConfigurablePin__SubclassingConfigurablePin__IsRecognized(self) -> None:
        # Arrange
        class DacPin(ConfigurablePin):
            def __init__(self, resolution: int) -> None:
                self.resolution = resolution
                self.capabilities = frozenset({AnalogOutput})
                self.mode = None

        # Act
        pin = DacPin(resolution=12)

        # Assert
        self.assertIsInstance(pin, ConfigurablePin)
        self.assertIsInstance(pin, Pin)
        self.assertEqual(pin.resolution, 12)
