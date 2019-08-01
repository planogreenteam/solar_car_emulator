#!/usr/bin/python3
import sys
import yaml
import time

from aux_battery import auxBattery
from motor_controller import motorController
from mppt import mppt
from panel_array import panelArray
from propulsion_motor import propulsionMotor
from propulsion_battery import propulsionBattery

# setup
def setup(argv):
    print('starting up the components')
    myAuxBatt = auxBattery()
    myMc = motorController()
    myMppt = mppt()
    myArray = panelArray()
    myMotor = propulsionMotor()
    myMainBatt = propulsionBattery()
    if argv[1] is not None:
        inputFile = argv[1]
        print("using input file: " + str(inputFile))
    else:
        print("no input file specified")


# main loop
def main():
    while(True):
        print('do stuff here')
        time.sleep(0.5)

# start!
if __name__ == "__main__":
    setup(sys.argv[1:])
    main()
