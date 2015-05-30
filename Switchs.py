#! /usr/bin/python

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Using BCM pinout
input_list = [22,23] #GPIO inputs for the switches
output_list = [6,13,19,26,12,16,20,21] #GPIO outputs for the steppers and in the future the laser led
GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(input_list, GPIO.BOTH)
GPIO.add_event_callback(input_list, GPIO.RISING, sw_rising)
GPIO.add_event_callback(input_list, GPIO.FALLING, sw_falling)

try:

    while True:
        def sw_rising(channel):
            print('Switch %s Rising'%channel)
        def sw_falling(channel):
            print('Switch %s Falling'%channel)


except KeyboardInterrupt:
        GPIO.cleanup()
        clear
        print "GoodBye"
