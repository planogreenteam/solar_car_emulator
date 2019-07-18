#!/usr/bin/python3

class motorController(object):
    def __init__(self):
        self.maxAmps = 200
        self.__state = "OK"

    @property
    def state(self):
        return self.__state
