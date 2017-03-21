#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TODO list:
    Raspberry
    Documentacao
'''

import os, subprocess, sys
from pyfirmata import Arduino, util

MIN = 0
MAX = 255
STEP = 10
DELAYMS = 10

OUTPIN = 'd:3:p'

port = None # '/dev/ttyACM0'

for file in os.listdir('/dev/'):
    if file.startswith('ttyACM'):
        port = os.path.join("/dev", file)
        break

if port == None:
    print 'Nenhum dispositivo reconhecido em /dev/ttyACM*'
    exit(1)
else:
    print 'Conectando a', port

board = Arduino(port)
out = board.get_pin(OUTPIN)

delay = DELAYMS/1000.0

p = None

try:
    while True:
        p = subprocess.Popen(['mpg123', '-q', 'ola.mp3'])
        p.wait()

        for i in xrange(MIN, MAX, STEP):
            value = i/float(MAX)
            out.write(value)
            board.pass_time(delay)

except KeyboardInterrupt:
    p.terminate()
    out.write(0)
    board.exit()
    exit()
