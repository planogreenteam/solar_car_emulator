#!/usr/bin/python3

class propulsionBattery(object):

    def __init__(self):
        self.__voltage = 48 # V
        self.__capacity = 4 # Ah
        self.__current = 200 #A

    @property
    def voltage(self):
        return self.__voltage

    @property
    def current(self):
        return self.__current

    @property
    def capacity(self):
        return self.__capacity
