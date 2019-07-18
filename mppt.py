#!/usr/bin/python3

class mppt(object):
    def __init__(self):
        self.__panelVoltage = 0
        self.__panelCurrent = 0
        self.__batteryVoltage = 48
        self.__batteryInputCurrent = 0

    @property
    def panelVoltage(self):
        return self.__panelVoltage

    @property
    def panelCurrent(self):
        return self.__panelCurrent

    @property
    def batteryVoltage(self):
        return self.__batteryVoltage

    @property
    def batteryInputCurrent(self):
        return self.__batteryInputCurrent
