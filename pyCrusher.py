#!/usr/bin/env python

###########################################################
#  Controls GPIO Pins and sensors for canCrusher project. #
###########################################################

# Import Mosdules
import RPi.GPIO as gpio
import time
import os
import sys
from subprocess import Popen
from subprocess import call


button = 7
crush = 23
retract = 24
bLED = 17
cLED = 27
rLED = 22
cLIMIT = 5
rLIMIT = 6
start_state = off_1

gpio.setmode(gpio.BCM)
gpio.setup(button, gpio.IN)
gpio.setup(cLIMIT, gpio.IN)
gpio.setup(rLIMIT, gpio.IN)
gpio.setup(crush, gpio.OUT)
gpio.setup(retract, gpio.OUT)
gpio.setup(bLED, gpio.OUT)
gpio.setup(cLED, gpio.OUT)
gpio.setup(rLED, gpio.OUT)

def return_home():
  


try:
  count = 0
  debounce = 0.4
  state = True
  previous = False
  current_state = start_state
  while True:
    reading = gpio.input(button)
    if reading == False and previous == False and time.time()-count > debounce:
      if state == True:
        state = False
      else:
        state = True
      count = time.time()
    gpio.output(bLED, state)
    if current_state == off_1:

    previous = reading

except:
  gpio.cleanup()
