#!/usr/bin/python3
import unittest
from aux_battery import auxBattery
from motor_controller import motorController
from panel_array import panelArray

class testAuxBattery(unittest.TestCase):
    def setUp(self):
        self.myAux = auxBattery()

    def tearDown(self):
        self.myAux = None

    def testGetVoltage(self):
        myVolts = self.myAux.getVoltage()
        assert myVolts is not None, "voltage was None"

    def testSetVoltage(self):
        testVoltage = 11.2
        self.myAux._auxBattery__setVoltage(testVoltage)
        myVolts = self.myAux.getVoltage()
        assert myVolts == testVoltage

    def testGetCapacity(self):
        myCap = self.myAux.getCapacity()
        assert myCap is not None, "voltage was None"

    def testSetCapacity(self):
        testCap = 1000
        self.myAux._auxBattery__setCapacity(testCap)
        myCap = self.myAux.getCapacity()
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
        assert myVolts is not None

    def testGetCurrent(self):
        myCurrent = self.myPanels.getCurrent()
        assert myCurrent is not None

if __name__=="__main__":
    unittest.main() #run all tests
