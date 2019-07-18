#!/usr/bin/python3

class propulsionMotor(object):

    def __init__(self):
        self.__current = 200
        self.__voltage = 48
        self.__rpm = 0

    def getCurrent(self):
        return self.__current

    def getVoltage(self):
        return self.__voltage

    def getRpm(self):
        return self.__rpm

    def __setCurrent(self, current):
        self.__current = current

    def __setRpm(self, rpm):
        self.__rpm = rpm
