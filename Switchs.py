#! /usr/bin/python

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Using BCM pinout
input_list = [22,23] #GPIO inputs for the switches
output_list = [6,13,19,26,12,16,20,21] #GPIO outputs for the steppers and in the future the laser led
GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(22, GPIO.BOTH)
GPIO.add_event_detect(23, GPIO.BOTH)
GPIO.add_event_callback(22, GPIO.RISING, sw01_rising)
GPIO.add_event_callback(22, GPIO.FALLING, sw01_falling)
GPIO.add_event_callback(23, GPIO.RISING, sw02_rising)
GPIO.add_event_callback(23, GPIO.FALLING, sw02_falling)
try:

    while True:
        def sw01_rising(channel):
            print('Switch %s Rising'%channel)
        def sw01_falling(channel):
            print('Switch %s Falling'%channel)
        def sw01_rising(channel):
            print('Switch %s Rising'%channel)
        def sw01_falling(channel):
            print('Switch %s Falling'%channel)



except KeyboardInterrupt:
        GPIO.cleanup()
        clear
        print "GoodBye"
