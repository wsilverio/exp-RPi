#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

'''
Botoes conectados nos pinos:
BCM 4 = BOARD pin 7
BCM 17 = BOARD pin 11
BCM 21 = BOARD pin 13
BCM 22 = BOARD pin 15
'''
BOTAO_ESQUERDA = 21 
BOTAO_DIREITA = 17
BOTAO_ENTER = 4
BOTAO_ESQ = 22

GPIO.setup(BOTAO_ESQUERDA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BOTAO_DIREITA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BOTAO_ENTER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BOTAO_ESQ, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

debouncing = 0.05

while True:
	if GPIO.input(BOTAO_ESQUERDA):
		print "Esquerda"
		sleep(debouncing)
		while GPIO.input(BOTAO_ESQUERDA): pass
	elif GPIO.input(BOTAO_DIREITA):
		print "Direita"
		sleep(debouncing)
		while GPIO.input(BOTAO_DIREITA): pass
	elif GPIO.input(BOTAO_ENTER):
		print "Enter"
		sleep(debouncing)
		while GPIO.input(BOTAO_ENTER): pass
	elif GPIO.input(BOTAO_ESQ):
		print "Esq"
		sleep(debouncing)
		while GPIO.input(BOTAO_ESQ): pass
	
	sleep(debouncing)
