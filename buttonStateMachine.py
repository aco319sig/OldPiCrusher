#!/usr/bin/env python

################################
#  Button State Machine Tester #
################################

import sys
import RPi.GPIO as gpio
import time
button7=7

state=0
gpio.setmode(gpio.BCM)
gpio.setup(button7, gpio.IN, gpio.PUD_UP)
gpio.setup(25, gpio.OUT)    #Yellow LED 2nd second
gpio.setup(24, gpio.OUT)    #Green LED 3RD SECOND

#########state machine loops#######################
def state0():
    if (gpio.input(7)==1):
        gpio.output(25, True)
        gpio.output(24, False)
        return 1
    else:
        return 0

def state1():
    if (gpio.input(7)==1):
        gpio.output(25, False)
        gpio.output(24, True)
        return 0
    else:
        return 1

#########################################################

if __name__ == '__main__':
    while True:
        if( state == 0 ):
            state=state0()
        elif( state == 1 ):
            state=state1()
        else:
            # catch invalid state setting
            print( "Invalid state" )
            break
        print( "State = ", state )
        # Now wait a while
        time.sleep(1)

#exit if invalid state
