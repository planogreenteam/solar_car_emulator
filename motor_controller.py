#!/usr/bin/python3

class motorController(object):
    def __init__(self):
        self.__maxAmps = 200
        self.__state = "OK"
        self.__capacity = 4 #Ah

    @property
    def maxAmps(self):
        return self.__maxAmps
