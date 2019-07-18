#!/usr/bin/python3

class motorController(object):
    def __init__(self):
        self.__maxAmps = 200
        self.__state = "OK"
        self.__capacity = 4 #Ah

    def getMaxAmps(self):
        return self.__maxAmps

    def setMaxAmps(self,maxAmps):
        self.__maxAmps = maxAmps
