import RPi.GPIO as gpio
import time

PINS = [6,13,19,26]

SEQA = [(22,),(22,21),(21,),(21,18),(18,),(18,17),(17,),(17,22)]
RSEQA = [(17,),(17,18),(18,),(18,21),(21,),(21,22),(22,),(22,17)]

DELAY = 0.002


gpio.setmode(gpio.BCM)
for pin in PINS:
    gpio.setup(pin, gpio.OUT)

def stepper(sequence, pins):
    for step in sequence:
        for pin in pins:
            gpio.output(pin, gpio.HIGH) if pin in step else gpio.output(pin, gpio.LOW)
        time.sleep(DELAY)


try:
    while True:
        for _ in xrange(512):
            stepper(SEQA,PINS)  # forward
        for _ in xrange(512):
            stepper(RSEQA,PINS)  # reverse
except KeyboardInterrupt:
    gpio.cleanup()
