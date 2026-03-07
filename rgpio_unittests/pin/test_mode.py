"""Tests for pin mode hierarchy, namespace, extensibility, and capabilities."""

from unittest import TestCase

from rgpio.pin.mode import (
    AnalogInput,
    AnalogOutput,
    CLK,
    CS,
    DigitalInput,
    DigitalOutput,
    Floating,
    I2C,
    MISO,
    MOSI,
    Modes,
    OpenDrain,
    PWM,
    PinMode,
    PullDown,
    PullUp,
    PushPull,
    RX,
    SCL,
    SDA,
    SPI,
    TX,
    UART,
)


class TestModeHierarchy(TestCase):
    """Tests for the PinMode class inheritance hierarchy."""

    def test_DigitalInput__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(DigitalInput, PinMode))

    def test_DigitalOutput__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(DigitalOutput, PinMode))

    def test_AnalogInput__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(AnalogInput, PinMode))

    def test_AnalogOutput__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(AnalogOutput, PinMode))

    def test_PWM__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(PWM, PinMode))

    def test_I2C__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(I2C, PinMode))

    def test_SPI__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(SPI, PinMode))

    def test_UART__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(UART, PinMode))

    def test_PullUp__IsSubclassOfDigitalInput__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(PullUp, DigitalInput))

    def test_PullDown__IsSubclassOfDigitalInput__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(PullDown, DigitalInput))

    def test_Floating__IsSubclassOfDigitalInput__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(Floating, DigitalInput))

    def test_PushPull__IsSubclassOfDigitalOutput__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(PushPull, DigitalOutput))

    def test_OpenDrain__IsSubclassOfDigitalOutput__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(OpenDrain, DigitalOutput))

    def test_SDA__IsSubclassOfI2C__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(SDA, I2C))

    def test_SCL__IsSubclassOfI2C__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(SCL, I2C))

    def test_MOSI__IsSubclassOfSPI__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(MOSI, SPI))

    def test_MISO__IsSubclassOfSPI__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(MISO, SPI))

    def test_CLK__IsSubclassOfSPI__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(CLK, SPI))

    def test_CS__IsSubclassOfSPI__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(CS, SPI))

    def test_TX__IsSubclassOfUART__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(TX, UART))

    def test_RX__IsSubclassOfUART__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(RX, UART))

    def test_PullUp__IsSubclassOfPinMode__ReturnsTrue(self) -> None:
        # Arrange & Act & Assert
        self.assertTrue(issubclass(PullUp, PinMode))

    def test_PullUp__IsNotSubclassOfDigitalOutput__ReturnsFalse(self) -> None:
        # Arrange & Act & Assert
        self.assertFalse(issubclass(PullUp, DigitalOutput))

    def test_DigitalInput__IsNotSubclassOfDigitalOutput__ReturnsFalse(self) -> None:
        # Arrange & Act & Assert
        self.assertFalse(issubclass(DigitalInput, DigitalOutput))

    def test_SDA__IsNotSubclassOfSPI__ReturnsFalse(self) -> None:
        # Arrange & Act & Assert
        self.assertFalse(issubclass(SDA, SPI))


class TestModeNamespace(TestCase):
    """Tests for namespace access to sub-modes via parent class attributes."""

    def test_DigitalInput__PullUpAttribute__IsPullUpClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(DigitalInput.PullUp, PullUp)

    def test_DigitalInput__PullDownAttribute__IsPullDownClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(DigitalInput.PullDown, PullDown)

    def test_DigitalInput__FloatingAttribute__IsFloatingClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(DigitalInput.Floating, Floating)

    def test_DigitalOutput__PushPullAttribute__IsPushPullClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(DigitalOutput.PushPull, PushPull)

    def test_DigitalOutput__OpenDrainAttribute__IsOpenDrainClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(DigitalOutput.OpenDrain, OpenDrain)

    def test_I2C__SDAAttribute__IsSDAClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(I2C.SDA, SDA)

    def test_I2C__SCLAttribute__IsSCLClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(I2C.SCL, SCL)

    def test_SPI__MOSIAttribute__IsMOSIClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(SPI.MOSI, MOSI)

    def test_SPI__MISOAttribute__IsMISOClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(SPI.MISO, MISO)

    def test_SPI__CLKAttribute__IsCLKClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(SPI.CLK, CLK)

    def test_SPI__CSAttribute__IsCSClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(SPI.CS, CS)

    def test_UART__TXAttribute__IsTXClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(UART.TX, TX)

    def test_UART__RXAttribute__IsRXClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(UART.RX, RX)


class TestModesNamespaceContainer(TestCase):
    """Tests for the Modes namespace container class."""

    def test_Modes__DigitalInputAttribute__IsDigitalInputClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.DigitalInput, DigitalInput)

    def test_Modes__DigitalOutputAttribute__IsDigitalOutputClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.DigitalOutput, DigitalOutput)

    def test_Modes__AnalogInputAttribute__IsAnalogInputClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.AnalogInput, AnalogInput)

    def test_Modes__AnalogOutputAttribute__IsAnalogOutputClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.AnalogOutput, AnalogOutput)

    def test_Modes__PWMAttribute__IsPWMClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.PWM, PWM)

    def test_Modes__I2CAttribute__IsI2CClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.I2C, I2C)

    def test_Modes__SPIAttribute__IsSPIClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.SPI, SPI)

    def test_Modes__UARTAttribute__IsUARTClass(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.UART, UART)

    def test_Modes__NestedAccess__DigitalInputPullUp(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.DigitalInput.PullUp, PullUp)

    def test_Modes__NestedAccess__SPIMosi(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.SPI.MOSI, MOSI)

    def test_Modes__NestedAccess__UARTTX(self) -> None:
        # Arrange & Act & Assert
        self.assertIs(Modes.UART.TX, TX)


class TestModeExtensibility(TestCase):
    """Tests for custom mode creation and auto-registration."""

    def test_CustomMode__SubclassingPinMode__IsSubclass(self) -> None:
        # Arrange
        class CustomMode(PinMode):
            pass

        # Act & Assert
        self.assertTrue(issubclass(CustomMode, PinMode))

    def test_CustomSubMode__SubclassingExistingMode__RegistersOnParent(self) -> None:
        # Arrange & Act
        class HighDrive(DigitalOutput):
            pass

        # Assert
        self.assertIs(DigitalOutput.HighDrive, HighDrive)

    def test_CustomSubMode__RegisterFalse__NotRegisteredOnParent(self) -> None:
        # Arrange & Act
        class HiddenMode(DigitalOutput, register=False):
            pass

        # Assert
        self.assertFalse(hasattr(DigitalOutput, "HiddenMode"))

    def test_CustomSubMode__IsSubclassOfParent__ReturnsTrue(self) -> None:
        # Arrange
        class CustomPullUp(DigitalInput):
            pass

        # Act & Assert
        self.assertTrue(issubclass(CustomPullUp, DigitalInput))
        self.assertTrue(issubclass(CustomPullUp, PinMode))

    def test_CustomNestedMode__TwoLevelsDeep__RegistersOnDirectParent(self) -> None:
        # Arrange
        class CustomBase(PinMode):
            pass

        # Act
        class CustomChild(CustomBase):
            pass

        # Assert
        self.assertIs(CustomBase.CustomChild, CustomChild)
        self.assertTrue(issubclass(CustomChild, PinMode))


class TestModeInstanceEquality(TestCase):
    """Tests for PinMode instance equality and hashing."""

    def test_Equality__SameType__InstancesAreEqual(self) -> None:
        # Arrange
        mode1 = PullUp()
        mode2 = PullUp()

        # Act & Assert
        self.assertEqual(mode1, mode2)

    def test_Equality__DifferentType__InstancesAreNotEqual(self) -> None:
        # Arrange
        mode1 = PullUp()
        mode2 = PWM()

        # Act & Assert
        self.assertNotEqual(mode1, mode2)

    def test_Equality__NonPinMode__ReturnsNotEqual(self) -> None:
        # Arrange
        mode = PullUp()

        # Act & Assert
        self.assertNotEqual(mode, "not a mode")

    def test_Hash__SameType__SameHash(self) -> None:
        # Arrange
        mode1 = PullUp()
        mode2 = PullUp()

        # Act & Assert
        self.assertEqual(hash(mode1), hash(mode2))

    def test_Hash__InstancesUsableInSet__DeduplicatesByType(self) -> None:
        # Arrange & Act
        modes = {PullUp(), PullUp(), PWM()}

        # Assert
        self.assertEqual(len(modes), 2)


class TestCapabilities(TestCase):
    """Tests for using modes in capability frozensets."""

    def test_Capabilities__FrozenSetOfModes__CreatesSuccessfully(self) -> None:
        # Arrange & Act
        caps = frozenset({DigitalInput.PullUp, DigitalInput.PullDown, PWM})

        # Assert
        self.assertEqual(len(caps), 3)

    def test_Capabilities__ContainmentCheck__FindsMode(self) -> None:
        # Arrange
        caps = frozenset({DigitalInput.PullUp, PWM})

        # Act & Assert
        self.assertIn(DigitalInput.PullUp, caps)
        self.assertIn(PWM, caps)

    def test_Capabilities__ContainmentCheck__DoesNotFindAbsentMode(self) -> None:
        # Arrange
        caps = frozenset({DigitalInput.PullUp, PWM})

        # Act & Assert
        self.assertNotIn(DigitalOutput.PushPull, caps)

    def test_Capabilities__IssubclassFilter__FindsCompatibleModes(self) -> None:
        # Arrange
        caps = frozenset(
            {DigitalInput.PullUp, DigitalInput.PullDown, PWM}
        )

        # Act
        digital_inputs = {m for m in caps if issubclass(m, DigitalInput)}

        # Assert
        self.assertEqual(digital_inputs, {DigitalInput.PullUp, DigitalInput.PullDown})

    def test_Capabilities__IssubclassFilter__NoMatchReturnsEmpty(self) -> None:
        # Arrange
        caps = frozenset({PWM, AnalogInput})

        # Act
        digital_inputs = {m for m in caps if issubclass(m, DigitalInput)}

        # Assert
        self.assertEqual(digital_inputs, set())

    def test_Capabilities__ModeViaNamespace__WorksInFrozenset(self) -> None:
        # Arrange & Act
        caps = frozenset(
            {Modes.DigitalInput.PullUp, Modes.PWM, Modes.I2C.SDA}
        )

        # Assert
        self.assertIn(PullUp, caps)
        self.assertIn(PWM, caps)
        self.assertIn(SDA, caps)


class TestCapabilityExactMatch(TestCase):
    """Tests verifying that parent and child modes are distinct capabilities.

    This is critical: capability checking uses exact match, NOT issubclass.
    A pin supporting DigitalInput does NOT implicitly support DigitalInput.PullUp,
    and vice versa.
    """

    def test_ExactMatch__ParentInCaps__ChildNotAccepted(self) -> None:
        # Arrange
        caps = frozenset({DigitalInput})

        # Act & Assert
        self.assertIn(DigitalInput, caps)
        self.assertNotIn(DigitalInput.PullUp, caps)
        self.assertNotIn(DigitalInput.PullDown, caps)
        self.assertNotIn(DigitalInput.Floating, caps)

    def test_ExactMatch__ChildInCaps__ParentNotAccepted(self) -> None:
        # Arrange
        caps = frozenset({DigitalInput.PullUp})

        # Act & Assert
        self.assertIn(DigitalInput.PullUp, caps)
        self.assertNotIn(DigitalInput, caps)

    def test_ExactMatch__SiblingModesAreDistinct(self) -> None:
        # Arrange
        caps = frozenset({DigitalInput.PullUp})

        # Act & Assert
        self.assertNotIn(DigitalInput.PullDown, caps)
        self.assertNotIn(DigitalInput.Floating, caps)

    def test_ExactMatch__ProtocolParentInCaps__RoleChildNotAccepted(self) -> None:
        # Arrange
        caps = frozenset({I2C})

        # Act & Assert
        self.assertIn(I2C, caps)
        self.assertNotIn(I2C.SDA, caps)
        self.assertNotIn(I2C.SCL, caps)

    def test_ExactMatch__ProtocolChildInCaps__ParentNotAccepted(self) -> None:
        # Arrange
        caps = frozenset({SPI.MOSI, SPI.CLK})

        # Act & Assert
        self.assertIn(SPI.MOSI, caps)
        self.assertIn(SPI.CLK, caps)
        self.assertNotIn(SPI, caps)
        self.assertNotIn(SPI.MISO, caps)

    def test_ExactMatch__IssubclassQueryStillWorks__DespiteExactMatch(self) -> None:
        """issubclass filtering is separate from exact-match containment."""
        # Arrange
        caps = frozenset({DigitalInput.PullUp})

        # Act
        has_any_digital_input = any(issubclass(m, DigitalInput) for m in caps)

        # Assert
        self.assertTrue(has_any_digital_input)
        self.assertNotIn(DigitalInput, caps)

    def test_ExactMatch__OutputParentInCaps__SubModesNotAccepted(self) -> None:
        # Arrange
        caps = frozenset({DigitalOutput})

        # Act & Assert
        self.assertIn(DigitalOutput, caps)
        self.assertNotIn(DigitalOutput.PushPull, caps)
        self.assertNotIn(DigitalOutput.OpenDrain, caps)

    def test_ExactMatch__MixedParentAndChild__BothPresent(self) -> None:
        # Arrange
        caps = frozenset({DigitalInput, DigitalInput.PullUp})

        # Act & Assert
        self.assertIn(DigitalInput, caps)
        self.assertIn(DigitalInput.PullUp, caps)
        self.assertNotIn(DigitalInput.PullDown, caps)
