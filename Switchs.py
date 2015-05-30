#! /usr/bin/python

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Using BCM pinout
input_list = [22,23] #GPIO inputs for the switches
output_list = [6,13,19,26,12,16,20,21] #GPIO outputs for the steppers and in the future the laser led
GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')
GPIO.add_event_detect(22, GPIO.RISING, callback=my_callback)

try:

    while True:
        ();

except KeyboardInterrupt:
        GPIO.cleanup()
        clear
        print "GoodBye"
