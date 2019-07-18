#!/usr/bin/python3

class panelArray(object):
    def __init__(self):
        self.__voltage = 48 # V
        self.__current = 8 # A

    def getVoltage(self):
        return self.__voltage

    def getCurrent(self):
        return self.__current

