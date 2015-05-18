#! /usr/bin/python

# please see wiki
# By Youenn Denis
software_version = '0.21.0'
print "Blacksad project v_%s" % software_version

# (c) Youenn Denis - MAY 2015

import smbus
import sys
import getopt
import time
bus = smbus.SMBus(1)
