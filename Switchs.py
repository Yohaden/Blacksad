#! /usr/bin/python

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Using BCM pinout
input_list = [22,23] #GPIO inputs for the switches
output_list = [6,13,19,26,12,16,20,21] #GPIO outputs for the steppers and in the future the laser led
GPIO.setup(input_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
def Sw01Press(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('The SW01 is pressed')
def Sw01Release(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('The SW01 is released')
def Sw02Press(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('The SW01 is pressed')
def Sw02Release(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('The SW01 is released')

GPIO.add_event_detect(22, GPIO.RISING, callback=Sw01Press, bouncetime=200)
GPIO.add_event_detect(22, GPIO.FALLING, callback=Sw01Release, bouncetime=200)
GPIO.add_event_detect(22, GPIO.RISING, callback=Sw02Press, bouncetime=200)
GPIO.add_event_detect(22, GPIO.RISING, callback=Sw02Release, bouncetime=200)

try:
    print "Press Ctrl C to quit"

except KeyboardInterrupt:
        GPIO.cleanup()
        clear
        print "GoodBye"
