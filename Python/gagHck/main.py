#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
from time import sleep

pin, std = int(sys.argv[1]), int(sys.argv[2])

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

#GPIO.output(pin, std)

if std > 1 :
	GPIO.output(pin,0)
	sleep(0.5)
	for i in xrange(std):
		GPIO.output(pin,True)
		sleep (0.1)
		GPIO.output(pin,False)
		sleep (0.1)
else:
	GPIO.output(pin, std)
