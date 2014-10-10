#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

'''
Botoes conectados nos pinos:
BCM 4 = BOARD pin 7
BCM 7 = BOARD pin 26
BCM 8 = BOARD pin 24
BCM 18 = BOARD pin 12
'''
BOTAO_ESQUERDA = 4 
BOTAO_DIREITA = 7
BOTAO_CIMA = 8
BOTAO_BAIXO = 18

GPIO.setup(BOTAO_ESQUERDA, GPIO.IN)
GPIO.setup(BOTAO_DIREITA, GPIO.IN)
GPIO.setup(BOTAO_CIMA, GPIO.IN)
GPIO.setup(BOTAO_BAIXO, GPIO.IN)

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
	elif GPIO.input(BOTAO_CIMA):
		print "Cima"
		sleep(debouncing)
		while GPIO.input(BOTAO_CIMA): pass
	elif GPIO.input(BOTAO_BAIXO):
		print "Baixo"
		sleep(debouncing)
		while GPIO.input(BOTAO_BAIXO): pass
	
	sleep(debouncing)
