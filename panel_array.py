#!/usr/bin/python3

class panelArray(object):
    def __init__(self):
        self.__voltage = 48 # V
        self.__current = 8 # A

    @property
    def voltage(self):
        return self.__voltage

    @property
    def current(self):
        return self.__current
