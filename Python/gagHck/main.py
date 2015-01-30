#!/usr/bin/python

import sys
import RPi.GPIO as GPIO

pin, std = int(sys.argv[1]), bool(sys.argv[2])

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, std)