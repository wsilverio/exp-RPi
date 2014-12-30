### Error Raspberry Pi: X11 connection rejected because of wrong authentication.  
  
$ ssh -X pi-user@ip  
$ xauth list  
$ su -  
$ touch ~/.Xauthority  
$ xauth add  
