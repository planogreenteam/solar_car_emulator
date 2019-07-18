#!/usr/bin/python3
import yaml
import time

from aux_battery import auxBattery
from motor_controller import motorController
from mppt import mppt
from panel_array import panelArray
from propulsion_motor import propulsionMotor
from propulsion_battery import propulsionBattery

# setup

# main loop
while(True):
    print('do stuff here')
    time.sleep(0.5)
