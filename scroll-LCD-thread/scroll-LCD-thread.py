#!/usr/bin/python

from time import sleep
from multiprocessing import Process, Queue
from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD()
lcd.begin(16,2)

def scroll(m):
	texto = ["", ""]
	i = j = imax = jmax = 0 # i e j: posicao da sub-string
	s = 1 # sentido da rotacao da linha de cima (1 = direita, -1: = esquerda)
	cont = 0 # contador de "frames": vel linha de cima = 2x vel linha de baixo
	
	while m.empty(): pass # aguarda a primeira "chamada"
	
	while True:
		if not m.empty():
			texto = m.get() # recebe as strings
			
			if (len(texto[0]) <= 16):
				lcd.home() # linha de cima
				lcd.message(texto[0].center(16)) # string fixa
			else:
				texto[0] += " "
				i = 0
				imax = len(texto[0]) - 16
				
			if (len(texto[1]) <= 16):
				lcd.setCursor(0,1) # linha de baixo
				lcd.message(texto[1].center(16)) # string fixa
			else:
				texto[1] = " "*16 + texto[1] + " "*16
				j = 0
				jmax = len(texto[1]) - 16

		if (len(texto[0]) > 16) and not (cont%2): # i
			lcd.home() # linha de cima
			sub_string = texto[0][i:i+16] # pega a fracao da string que cabe no LCD
			lcd.message(sub_string) # escreve no display
			i += s # direcao (direita ou esquerda)
			if (i < 0) or (i >= imax): s = -s # inverte a direcao se atingir os limites do display
		
		if (len(texto[1]) > 16): # j
			lcd.setCursor(0,1) # linha de baixo
			sub_string = texto[1][j:j+16] # pega a fracao da string que cabe no LCD
			lcd.message(sub_string) # escreve no display
			j += 1 # proxima posicao a direita
			if (j >= jmax): j = 0 # primeira posicao caso atinja os limites do display			
	
		sleep(0.1)
		cont += 1

msg = Queue()

p = Process(target=scroll, args=(msg,))
p.start()

while True:
	cima = raw_input("Linha 0: ") # string a ser escrita na linha de cima
	baixo = raw_input("Linha 1: ") # string a ser escrita na linha de baixo
	
	msg.put([cima, baixo])