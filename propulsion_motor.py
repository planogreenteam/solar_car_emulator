#!/usr/bin/python3

class propulsionMotor(object):

    def __init__(self):
        self.__current = 200
        self.__voltage = 48
        self.__rpm = 0

    @property
    def current(self):
        return self.__current

    @property
    def voltage(self):
        return self.__voltage

    @property
    def rpm(self):
        return self.__rpm
