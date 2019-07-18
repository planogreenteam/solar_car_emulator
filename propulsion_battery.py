#!/usr/bin/python3

class propulsionBattery(object):

    def __init__(self):
        self.__voltage = 48 # V
        self.__capacity = 4 # Ah
        self.__current = 200 #A

    def getVoltage(self):
        return self.__voltage

    def getCurrent(self):
        return self.__current

    def getCapacity(self):
        return self.__capacity

    def __setVoltage(self, voltage):
        self.__voltage = voltage

    def __setCurrent(self, current):
        self.__current = current

    def __setCapacity(self, capacity):
        self.__capacity = capacity
