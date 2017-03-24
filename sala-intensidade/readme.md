##### TODO list:
- Leitura dos sensores com gpio
- Instalador automático
- Lançar o programa no boot

### Arduino:

Carregue o sketch [Standard Firmata](https://github.com/firmata/arduino/blob/master/examples/StandardFirmata/StandardFirmata.ino):
`File >> Examples >> Firmata >> StandardFirmata`

### Raspberry Pi:

Montar a partição `boot` e habilitar a conexão ssh:
```
touch ssh
```

Acessar o Raspberry Pi:
```
ssh pi@ip
$ raspberry
```

<!--
Atualize o sistema:
```
sudo apt-get update -y
sudo apt-get upgrade -y
```

Instale os drivers **Alsa** e o player MP3 **mpg123**:
```
sudo apt-get install alsa-utils mpg123
```

Instale o pacote **python-dev**:
```
sudo apt-get install python-dev
```

Instale o pacote **python-rpi.gpio**:
```
sudo apt-get install python-rpi.gpio
```

Instale o instalador(!) de pacotes **pip**:
```
sudo apt-get install python-pip
```

Instale o pacote **pyFirmata**:
```
sudo pip install pyfirmata
```
-->

Execute o instalador automático:

```
bash <(curl -s https://raw.githubusercontent.com/wsilverio/exp-RPi/master/sala-intensidade/autoinstall.sh)
```


Reinicie o sistema:
```
sudo reboot
```

Carregue os drivers e configure a saída de audio (jack 3.5mm):
```
sudo modprobe snd_bcm2835
sudo amixer cset numid=3 1
```
