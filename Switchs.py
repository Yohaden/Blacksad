#! /usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.IN)
GPIO.setup(23,GPIO.IN)

if (GPIO.input(22)):
    print("Button 1 Pressed");

if (GPIO.input(23)):
        print("Button 2 Pressed");
