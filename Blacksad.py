#! /usr/bin/python

# please see wiki
# By Youenn Denis
software_version = '0.21.0'
print 'Blacksad project version' software_version

# © Youenn Denis - MAY 2015

import smbus
import sys
import getopt
import time
bus = smbus.SMBus(1)
