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
irBreakBeam = 8
cMODE = 23
rMODE = 24
irLED = 2
bLED = 17
cLED = 27
rLED = 22
cLIMIT = 5
rLIMIT = 6
# cSTATE = ""
# rSTATE = ""
tgt = ""
pressed = ""


def Main():
  global button, pressed

  pressed = False
  b_Ready = True
  setup()
  selfTest()
  retract()
  gpio.add_event_detect(button, gpio.RISING, callback=state_check)





def state_check(channel):
  global button, pressed, irBreakBeam
  while True:
    if b_Ready and gpio.input(button, gpio.HIGH) and gpio.input(irBreakBeam, gpio.LOW):
      pressed = True
      b_Ready = False
      while gpio.input(irBreakBeam, gpio.LOW):
        crush()
        retract()
        time.sleep(2)

    elif b_Ready and gpio.input(button, gpio.HIGH) and gpio.input(irBreakBeam, gpio.HIGH):
      flash_LED(irLED)
      flash_LED(bLED)
      b_Ready = True
      pressed = False
      gpio.remove_event_detect(button)

    time.sleep(0.01)


def setup():
  gpio.setmode(gpio.BCM)
  gpio.setup(button, gpio.IN, pull_up_down=gpio.PUD_DOWN)
  gpio.setup(irBreakBeam, gpio.IN, pull_up_down=gpio.PUD_UP)
  gpio.setup(cLIMIT, gpio.IN, pull_up_down=gpio.PUD_UP)
  gpio.setup(rLIMIT, gpio.IN, pull_up_down=gpio.PUD_UP)
  gpio.setup(cMODE, gpio.OUT)
  gpio.setup(rMODE, gpio.OUT)
  gpio.setup(irLED, gpio.OUT)
  gpio.setup(bLED, gpio.OUT)
  gpio.setup(cLED, gpio.OUT)
  gpio.setup(rLED, gpio.OUT)


def selfTest():
  global bLED, cLED, rLED
  gpio.output(bLED, gpio.HIGH)
  gpio.output(cLED, gpio.HIGH)
  gpio.output(rLED, gpio.HIGH)
  time.sleep(1.00)
  gpio.output(bLED, gpio.LOW)
  gpio.output(cLED, gpio.LOW)
  gpio.output(rLED, gpio.LOW)
  time.sleep(1.00)
  gpio.output(bLED, gpio.HIGH)
  gpio.output(cLED, gpio.HIGH)
  gpio.output(rLED, gpio.HIGH)
  time.sleep(1.00)
  gpio.output(bLED, gpio.LOW)
  gpio.output(cLED, gpio.LOW)
  gpio.output(rLED, gpio.LOW)


def retract():
  global rMODE, rLED, rLIMIT

  # check if limit switch tripped.
  while True:
    if gpio.input(rLIMIT) == gpio.HIGH:
      gpio.output(rMODE, gpio.HIGH)
      gpio.output(rLED, gpio.HIGH)
    else:
      flash_LED(rLED)
    time.sleep(0.01)


def crush():
  global cMODE, cLED, cLIMIT
  # if limit switch not tripped
  while True:
    if gpio.input(cLIMIT) == gpio.HIGH:
      gpio.output(cMODE, gpio.HIGH)
      gpio.output(cLED, gpio.HIGH)
    else:
      flash_LED(cLED)
    time.sleep(0.01)


def flash_LED(tgt):
  global rLED
  #Flash the LED
  gpio.output(tgt, gpio.HIGH)
  time.sleep(0.1)
  gpio.output(tgt, gpio.LOW)
  time.sleep(0.1)
  gpio.output(tgt, gpio.HIGH)
  time.sleep(0.1)
  gpio.output(tgt, gpio.LOW)
  time.sleep(0.1)
  gpio.output(tgt, gpio.HIGH)
  time.sleep(0.1)
  gpio.output(tgt, gpio.LOW)
  time.sleep(0.1)
  gpio.output(tgt, gpio.HIGH)
  time.sleep(0.1)
  gpio.output(tgt, gpio.LOW)
  time.sleep(0.1)
  gpio.output(tgt, gpio.HIGH)
  time.sleep(0.1)
  gpio.output(tgt, gpio.LOW)


# def readButton():
#
#   try:
#     count = 0
#     debounce = 0.4
#     state = True
#     previous = False
#     current_state = start_state
#     while True:
#       reading = gpio.input(button)
#       if reading == False and previous == False and time.time()-count > debounce:
#         if state == True:
#           state = False
#         else:
#           state = True
#         count = time.time()
#       gpio.output(bLED, state)
#       if current_state == off_1:
#
#     previous = reading
#
#   except:
#         gpio.cleanup()
