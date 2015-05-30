#! /usr/bin/python

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Using BCM pinout
input_list = [22,23] #GPIO inputs for the switches
output_list = [6,12,13,16,19,20,21,26] #GPIO outputs for the steppers and in the future the laser led
GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
def Sw01action(channel):
    if GPIO.input(22):
        print('This is a edge event callback function!')
        print('Edge detected on channel %s'%channel)
        print('The SW01 is pressed')
    else:
        print('This is a edge event callback function!')
        print('Edge detected on channel %s'%channel)
        print('The SW01 is released')

def Sw02action(channel):
    if GPIO.input(23):
        print('This is a edge event callback function!')
        print('Edge detected on channel %s'%channel)
        print('The SW02 is pressed')
    else:
        print('This is a edge event callback function!')
        print('Edge detected on channel %s'%channel)
        print('The SW02 is released')


GPIO.add_event_detect(22, GPIO.BOTH, callback=Sw01action, bouncetime=200)
GPIO.add_event_detect(23, GPIO.BOTH, callback=Sw02action, bouncetime=200)

try:
    while True:
        pass


except KeyboardInterrupt:
        GPIO.cleanup()
        print "GoodBye"
