#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TODO list:
    Raspberry
    Documentacao
'''
import os, subprocess, sys, time, threading

def checkPort():
    port = None
    for file in os.listdir('/dev/'):
        if file.startswith('ttyACM') or file.startswith('ttyUSB'):
            port = os.path.join("/dev", file)
            break
            # PORT.append(os.path.join("/dev", file))
    return port

VOICE_FILE = './voz.mp3' # Localização do arquivo de voz

isRasp = True       # Raspberry Pi plataforma
hasFirmata = True   # Firmata modulo

MIN = 0             # PWM max
MAX = 255           # PWM min
STEP = 10           # PWM passo
DELAYMS = 10        # Delay (ms)

OUTPIN = 'd:3:p'    # Arduino pino
PORT = checkPort()  # Arduino porta ('/dev/ttyUSBx' or '/dev/ttyACMx')

INPIN = 7           # Raspberry pino (número no conector)

try:
    from pyfirmata import Arduino, util
except ImportError:
    hasFirmata = False

if not hasFirmata:
    print "Módulo firmata não encontrado."

try:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) # Números dos pinos no conector
    GPIO.setup(INPIN, GPIO.IN)
    print "Plataforma: Raspberry Pi\n"
except ImportError:
    isRasp = False
    print "Plataforma: Não Raspberry Pi\n"

i = 0
while PORT == None:
    print 'Nenhum dispositivo reconhecido em /dev/ttyACM* ou /dev/ttyUSB*'
    print 'Por favor, conecte um Arduino à porta USB {%d}\n' %i
    i += 1
    PORT = checkPort()
    time.sleep(5)

print 'Conectando a', PORT

board = None
out = None

if hasFirmata:
    board = Arduino(PORT)
    out = board.get_pin(OUTPIN)

p = None
delay = DELAYMS/1000.0

try:
    while True:

        if isRasp:
            
            if GPIO.input(INPIN) == 1: # Movimento detectado
                pass

        else:
            pass

        p = subprocess.Popen(['mpg123', '-q', VOICE_FILE])
        p.wait()

        if hasFirmata:
            for i in xrange(MIN, MAX, STEP):
                value = i/float(MAX)
                out.write(value)
                board.pass_time(delay)

except KeyboardInterrupt:
    p.terminate()
    if hasFirmata:
        out.write(0)
    board.exit()
    exit()
