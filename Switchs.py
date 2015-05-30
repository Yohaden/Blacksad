#! /usr/bin/python

import sys
import time

#Avoiding crashing
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        try:
            sys.exit(0)
            GPIO.cleanup()
        except SystemExit:
            os._exit(0)

            import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Using BCM pinout
input_list = [22,23] #GPIO inputs for the switches
output_list = [6,13,19,26,12,16,20,21] #GPIO outputs for the steppers and in the future the laser led
GPIO.setup(input_list,GPIO.IN pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_list,GPIO.OUT, initial=GPIO.LOW)

    if (GPIO.input(22)):
        print("Button 1 Pressed");

    if (GPIO.input(23)):
        print("Button 2 Pressed");
