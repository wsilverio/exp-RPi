### Error Raspberry Pi: X11 connection rejected because of wrong authentication.  
  
  
Solucao:  
Conexao via ssh *troque 'ip' pelo ip do RPi*:  
$ ssh -X pi-user@ip  
  
Lista as autorizacoes do servidor X:  
$ xauth list  
Resultado, exemplo:  
maq-rpi/unix:11  MIT-MAGIC-COOKIE-1  wyr30a3qlhqv8ihf2bg3f6rvg2hwl9p3  
  
Login como root  
$ su -  
  
Cria o arquivo Xauthority:  
$ touch ~/.Xauthority  
  
Entrada de autorizacao, exemplo:  
$ xauth add maq-rpi/unix:11  MIT-MAGIC-COOKIE-1  wyr30a3qlhqv8ihf2bg3f6rvg2hwl9p3  
  
Teste, exemplo:    
$ sudo leafpad /etc/network/interfaces  
