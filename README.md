# PilotScan
Firmware

Activar gateway:
$ sudo route add default gw 172.17.91.1


Comunicacion nuc a micro
NUC:
El protocolo se construye a partir de una tabal de valores contantes que indican el estado de diferentes señales.
El primer Byte corresponde al perifierico del cual se desea informar del estado; el segundo byte para este caso, corresponde a los estados basicos de operacion (no conectado, inicializando, funcionando) y algunos otros como el porcentaje de sinconismo del GPS entre otros.
Si el primer Byte esta en 0, el mesaje de incormacion corresponde a informacion del sistema o acciones sobre el hardware codificadas en el segundo Byte.

Micro:
El dato llega como un entero codificado de 4bytes, los dos primero son la informacion codificada mientras que los otros corresponden a 2 bytes de verificacion (checksum) los cuales corresponden a la suma de los dos primero bytes, esto con el objetivo de verificar que la informacion recibida corresponde efectivamente a al enviada por la NUC.


Comunicaion micro a nuc
Micro:
El protocolo consta de tres Bytes y dos modos de funcionamiento. El primero consiste en enviar la informacion adquirida por los sensores, mientra el segundo envia comandos de sistema que debe ejecutar la NUC.
El modo 1 se puede subdividir de igual forma en dos tipos, los cuales estan estructurados como,

Modo 1.a: Numeros inferiores a 16.0
- El priemro es indica la variable que se va a transmitir.
- El segundo corresponde a la parte entera del valor a enviar.
- El tercero corresponde a la parte decimal del valor a enviar.

Modo 1.b: Numeros superiores a 16
- El priemro es indica la variable que se va a transmitir.
- El segundo y el tercero corresponden a un numero entero de 2 bytes [0 255] que corresponde al valor a enviar.

Modo 2:
- El priemro que es 'a', indica un mensaje de tipo instruccion para la NUC.
- El segundo y el tercero corresponden a una codificacion de diferentes tipos de acciones que se puede solicitar desde microcontrolador a la NUC.
