#!/bin/bash

PACOTES_APT="alsa-utils mpg123 python-dev python-rpi.gpio python-pip"
PACOTES_PIP="pyfirmata"

# sudo apt-get update -y
# sudo apt-get install -y $PACOTES_APT
# sudo pip install $PACOTES_PIP

# sudo modprobe snd_bcm2835
# sudo amixer cset numid=3 1

echo $PACOTES_PIP
echo $PACOTES_APT
