#!/usr/bin/python3
import unittest
from aux_battery import auxBattery
from motor_controller import motorController
from panel_array import panelArray
from propulsion_battery import propulsionBattery
from propulsion_motor import propulsionMotor
from mppt import mppt

class testAuxBattery(unittest.TestCase):
    def setUp(self):
        self.myAux = auxBattery()

    def tearDown(self):
        self.myAux = None

    def testGetVoltage(self):
        myVolts = self.myAux.voltage
        assert myVolts is not None, "voltage was None"

    def testSetVoltage(self):
        testVoltage = 11.2
        self.myAux._auxBattery__voltage = testVoltage
        myVolts = self.myAux.voltage
        assert myVolts == testVoltage

    def testGetCapacity(self):
        myCap = self.myAux.capacity
        assert myCap is not None, "voltage was None"

    def testSetCapacity(self):
        testCap = 1000
        self.myAux._auxBattery__capacity = testCap
        myCap = self.myAux.capacity
        assert myCap == testCap, "input capacity did not equal output capacity"

class testMotorController(unittest.TestCase):
    def setUp(self):
        self.myMc = motorController()

    def tearDown(self):
        self.myMc = None

    def testGetMaxAmps(self):
        myMaxAmps = self.myMc.getMaxAmps()
        assert myMaxAmps is not None, "max amps is None"
        
    def testSetMaxAmps(self):
        testMaxAmps = 200
        self.myMc.setMaxAmps(testMaxAmps)
        myMax = self.myMc.getMaxAmps()
        assert myMax == testMaxAmps, "max amps input does not match output"

class testPanelArray(unittest.TestCase):
    def setUp(self):
        self.myPanels = panelArray()

    def tearDown(self):
        self.myPanels = None

    def testGetVoltage(self):
        myVolts = self.myPanels.getVoltage()
        assert myVolts is not None, "voltage is none"

    def testGetCurrent(self):
        myCurrent = self.myPanels.getCurrent()
        assert myCurrent is not None, "current is none"

    def testSetVoltage(self):
        testVolts = 33
        self.myPanels._panelArray__setVoltage(testVolts)
        myVolts = self.myPanels.getVoltage()
        assert myVolts == testVolts, "input volts does not equal output volts"

    def testSetCurrent(self):
        testCurrent = 7
        self.myPanels._panelArray__setCurrent(testCurrent)
        myCurrent = self.myPanels.getCurrent()
        assert myCurrent == testCurrent, "input current does not equal output current"

class testPropulsionBattery(unittest.TestCase):
    def setUp(self):
        self.myBat = propulsionBattery()

    def tearDown(self):
        self.myBat = None

    def testGetVoltage(self):
        myVolts = self.myBat.getVoltage()
        assert myVolts is not None, "volts was none"

    def testGetCurrent(self):
        myAmps = self.myBat.getCurrent()
        assert myAmps is not None, "amps was none"

    def testGetCapacity(self):
        myCap = self.myBat.getCapacity()
        assert myCap is not None, "capacity was none"

    def testSetVoltage(self):
        testVolts = 31
        self.myBat._propulsionBattery__setVoltage(testVolts)
        myVolts = self.myBat.getVoltage()
        assert myVolts == testVolts, "input voltage not equal to output voltage"

    def testSetCurrent(self):
        testAmps = 122
        self.myBat._propulsionBattery__setCurrent(testAmps)
        myAmps = self.myBat.getCurrent()
        assert myAmps == testAmps, "input current not equal to output current"

    def testSetCapacity(self):
        testCap = 1.11111
        self.myBat._propulsionBattery__setCapacity(testCap)
        myCap = self.myBat.getCapacity()
        assert myCap == testCap, "input capacity not equal to output current"

class testPropulsionMotor(unittest.TestCase):
    def setUp(self):
        self.myMotor = propulsionMotor()

    def tearDown(self):
        self.myMotor = None

    def testGetVoltage(self):
        myVolts = self.myMotor.getVoltage()
        assert myVolts is not None, "volts is None"

    def testGetCurrent(self):
        myAmps = self.myMotor.getCurrent()
        assert myAmps is not None, "amps is None"

    def testGetRpm(self):
        myRpm = self.myMotor.getRpm()
        assert myRpm is not None

    def testSetCurrent(self):
        testAmps = 37
        self.myMotor._propulsionMotor__setCurrent(testAmps)
        myAmps = self.myMotor.getCurrent()
        assert myAmps == testAmps,"input amps not equal to output amps"

    def testSetRpm(self):
        testRpm = 1000
        self.myMotor._propulsionMotor__setRpm(testRpm)
        myRpm = self.myMotor.getRpm()
        assert myRpm == testRpm,"input rpm not equal to output rpm"

class testMppt(unittest.TestCase):
    def setUp(self):
        self.myTracker = mppt()

    def tearDown(self):
        self.myTracker = None

    def testGetPanelVoltage(self):
        myVolts = self.myTracker.panelVoltage
        assert myVolts is not None, "volts is none"

    def testSetPanelVoltage(self):
        testVolts = 32
        self.myTracker._mppt__panelVoltage = testVolts
        myVolts = self.myTracker.panelVoltage
        assert myVolts == testVolts, "input panel voltage does not equal output panel voltage"

    def testGetPanelCurrent(self):
        myAmps = self.myTracker.panelCurrent
        assert myAmps is not None, "amps is none"

    def testSetPanelCurrent(self):
        testAmps = 199
        self.myTracker._mppt__panelCurrent = testAmps
        myAmps = self.myTracker.panelCurrent
        assert myAmps == testAmps, "input panel current does not equal output panel current"

    def testGetBatteryVoltage(self):
        myVolts = self.myTracker.batteryVoltage
        assert myVolts is not None, "volts is none"

    def testSetBattertVoltage(self):
        testVolts = 34
        self.myTracker._mppt__batteryVoltage = testVolts
        myVolts = self.myTracker.batteryVoltage
        assert myVolts == testVolts, "input volts does not equal output volts"

    def testGetBatteryInputCurrent(self):
        myAmps = self.myTracker.batteryInputCurrent
        assert myAmps is not None, "amps is none"

    def testSetBatteryInputCurrent(self):
        testAmps = 193
        self.myTracker._mppt__batteryInputCurrent = testAmps
        myAmps = self.myTracker.batteryInputCurrent
        assert myAmps == testAmps, "input amps not equal to output amps"

if __name__=="__main__":
    unittest.main() #run all tests
