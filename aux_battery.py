#!/usr/bin/python3

class auxBattery(object):
    def __init__(self):
        self.__threshold = 13.3 #V
        self.__voltage = 14.4 #V
        self.__capacity = 3000 #mAh

    def getVoltage(self):
        return self.__voltage

    def __setVoltage(self,voltage):
        self.__voltage = voltage

    def getCapacity(self):
        return self.__capacity

    def __setCapacity(self,capacity):
        self.__capacity = capacity
