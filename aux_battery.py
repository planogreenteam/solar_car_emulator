#!/usr/bin/python3

class auxBattery(object):
    def __init__(self):
        self.__threshold = 13.3 #V
        self.__voltage = 14.4 #V
        self.__capacity = 3000 #mAh

    @property
    def voltage(self):
        return self.__voltage

    @property
    def capacity(self):
        return self.__capacity

    @property
    def capacity(self):
        return self.__capacity

