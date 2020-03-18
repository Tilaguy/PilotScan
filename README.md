## PILOT SCAN
---
En construccion
---
### Software Installation

##### System_monitor Installation
Insatalacion del System_monitor node: (https://github.com/RobotnikAutomation/system_monitor)

Dentro de la carpeta src del workspace se descarga el system monitor usando la siguiente instruccion:
~~~
$ git clone https://github.com/RobotnikAutomation/system_monitor
~~~
Luego se regresa al workspace y se compila usando la instruccion 
~~~
$ catkin_make
~~~
Acto seguido se instalan algunas dependencias necesarias para la ejecucion usando las siguientes instrucciones:
~~~
$ sudo apt-get install sysstat ifstat ntpdate
~~~
Por ultimo, para correr el nodo usamos la instruccion:
~~~
$ roslaunch system_monitor system_monitor.launch
~~~
### Comunicacion NUC-Micro 
##### NUC 
El protocolo se construye a partir de una tabla de valores contantes las cuales indican el estado de diferentes señales de sistema tales como el encendido el funcionamiento u otras opciones de los perifericos. El primer Byte (data 1) corresponde al perifierico el cual informa su estado, el segundo Byte (data 2) realiza una funcion dependiendo del periferico, sin embargo cuando data1 y data2 son 0 (cero) significa un error en el periferico, de igual manera el error es emitido por medio de un led RGB el cual se ha asignado un color especifico dependiedo del error y su color se especifica en cada tabla.

##### Micro
El dato llega como un entero codificado de 4 (cuatro) Bytes, los primeros 2 (dos) Bytes son la informacion codificada mientras que los otros 2 (dos) Bytes corresponden a Bytes de verificacion llamados checksum, estos corresponden a la suma de los 2 (dos) primeros Bytes, esto con el objetivo de verificar que la informacion recibida corresponde efectivamente a la enviada por la NUC.

#### Tabla de los mensajes del sistema

data 1 | data 2 | message | meaning| R | G | B
-- | -- | -- | -- | -- | -- | -- 
0 | 0 |         |Reserve|0|0|0
0 | 1 | sys-on_24 |	Turn-on source 24V
0 | 2 | sys-off_12 |Turn-off source 12V
0 | 3 | sys-off_24 |Turn-off source 24V
0 | 4 | sys-mem_E |	Memory problem
0 | 5 | sys-on_m8 |	Turn LiDAR on
0 | 6 | sys-on_tty |Turn all tty ports on
0 | 7 |
0 | 8 |
0 | 9 |
0 | A |
0 | B |
0 | C |
0 | D |
0 | E |
0 | F |

### Tabla del VN300
data 1 | data 2 | message | meaning | R | G | B |N/LED
-- | -- | -- | -- | -- | -- | -- |--
1 | 0 |         |Reserve|0|0|0
1 | 1 | VN300-NC |	VN300 No Connected|240|0|0|L1
1 | 2 | VN300-Start |VN 300 Starting|240|128|0|L1
1 | 3 | VN300-<25 | VN300 <25%|50|0|240|L1
1 | 4 | VN300-<50 |25% < VN300 <50%|50|80|160|L1
1 | 5 | VN300-<75 |	50% < VN300 <75|50|160|80|L1
1 | 6 | VN300->75 |VN300 >75%|50|240|0|L1
1 | 7 |VN300-Work | VN300 Working|0|240|0|L1
1 | 8 |
1 | 9 |
1 | A |
1 | B |
1 | C |
1 | D |
1 | E |
1 | F |

### Tabla del M8 LiDAR
data 1 | data 2 | message | meaning | R | G | B |N/LED
-- | -- | -- | -- | -- | -- | -- | --
2 | 0 |         |Reserve|0|0|0
2 | 1 | M8-NC |	M8 No Ping|240	|0|0|L2
2 | 2 | M8-Start |M8 Starting|240|128|0|L2
2 | 3 |  | ||||L2
2 | 4 |  | ||||L2
2 | 5 |  | ||||L2
2 | 6 |  | ||||L2
2 | 7 |M8-Work | M8 Working|0|240|0 |L2
2 | 8 |
2 | 9 |
2 | A |
2 | B |
2 | C |
2 | D |
2 | E |
2 | F |
### Tabla de la Camara
data 1 | data 2 | message | meaning | R | G | B
-- | -- | -- | -- | -- | -- | -- 
3 | 0 |         |Reserve|0|0|0
3 | 1 | CAM-NC | CAM No Connected
3 | 2 | CAM-Start |CAM Starting
3 | 3 |  |
3 | 4 |  |
3 | 5 |  |
3 | 6 |  |
3 | 7 |CAM-Work | CAM Working
3 | 8 |
3 | 9 |
3 | A |
3 | B |
3 | C |
3 | D |
3 | E |
3 | F |
### Tabla de Fuzzi-Temp
data 1 | data 2 | message | meaning | R | G | B
-- | -- | -- | -- | -- | -- | -- 
3 | 0 |  |Reserve|0|0|0
3 | 1 |   
3 | 2 |  
3 | 3 |  
3 | 4 |  
3 | 5 |  
3 | 6 |  
3 | 7 |   
3 | 8 |
3 | 9 |
3 | A |
3 | B |
3 | C |FUZZ-T1|>25°|13	|0|	125
3 | D |FUZZ-T2|>30°|113|	0|	125
3 | E |FUZZ-T3|>35°|255|	128|	0
3 | F |FUZZ-T4|>40°|250|0|	0
### Tabla errores de memoria
data 1 | data 2 | message | meaning | R | G | B |N/LED
-- | -- | -- | -- | -- | -- | -- | --
A | 0 |  |Reserve|0|0|0
A | 1 | memo-RAM_E1 |RAM alert1|255|64|64|L3
A | 2 | memo-RAM_E2 |RAM alert2|255|0|0|L3
A | 3 |  |||||L3
A | 4 |  |||||L3
A | 5 |  |||||L3
A | 6 | memo-ROM_E1 |ROM alert1|64|133|255 |L3
A | 7 | memo-ROM_E2 |ROM alert2|64|64|255|L3
A | 8 | memo-ROM_E3 |ROM alert3|0|0|255|L3
A | 9 |
A | A |
A | B |
A | C |
A | D |
A | E |
A | F |

#### Comunicacion Micro-NUC
Este protocolo consta de tres Bytes y dos modos de funcionamiento. El primer modo (Modo 1) consiste en enviar la informacion adquirida por los sensores, mientras que el segundo modo (Modo 2) envia comandos de sistema que la NUC debe ejecutar. Ademas el primer modo se puede subdividir de igual forma en dos tipos, estos estan estructurados como:
##### Modo 1.a
Este modo corresponde cuando el valor a enviar es inferior a 16.0, por lo tanto el orden del menseja es tal que:
* El primer Byte indica la variable a transmitir
* El segundo Byte corresponde a la parte entera del valor a enviar
* El tercer Byte corresponde a la parte decimal del valor a enviar
##### Modo 1.b
Este modo corresponde cuando el valor a enviar es superior a 16
* El primer Byte indica la variable a transmitir
* El segundo Byte y el tercer Byte corresponden a un numero entero de dos Bytes(en un rango de 0 a 255) el cual corresponde al valor a enviar

Este protocolo posee un mensaje de error en los perifericos o el sistema cuando Command, data1 y data2 son 0 (Cero).
#### Tabla 1
   
Command|	data1|	data2|	meaning|
|--|--|--|--|
0|	|	|	Reserved|
1|	x|	y|	current source 5 "x.y"|
2|	x|	y|	current source 12 "x.y"|
3|	x|	y|	current source 24 "x.y"|
4|	x|	y|	current source battery "x.y"|
5|	x|	y|	Voltage source 5 "x.y"|
6|	x|	y|	Voltage source 12 "x.y"|
7|	x|	y|	Voltage source 24 "x.y"|
8|	x|	y|	Voltage source Battery "x.y"|
9|	x|	y|	Temperature LiDAR|
A|	x|	y|	Temperature dsPIC|
B|	x|	y|	Temperature DC|
C|	x|	y|	Temperature xx|
D|	x|	y|	Hight|
#### Modo 2
* El primer Byte que es 'F', indica un mensaje de tipo instruccion para la NUC
* El segundo y el tercero corresponden a un codificacion de diferentes tipos de acciones que se puede solicitar desde el microcontrolador a la NUC.
#### Tabla 2
|Command|	data1|	data2|	meaning|
|--|--|--|--|
|F	|0	|0	|Reserved|
|F	|0	|1	|12 V is on|
|F	|1	|0	|24 V is on|
|F	|1	|1	|All sources are on|
|F	|0	|2	|12 V is going to shut it down in 1 m|
|F	|2	|0	|24 V is going to shut it down in 1 m|
|F	|2	|2	|All sources are going to shut it down in 1 m|
|F	|0	|3	|shut LiDAR down |
|F	|3	|0	|close all tty ports|
|F	|3	|3	|shut ROS down |
|F	|0	|4	|turn LiDAR on|
|F	|4	|0	|turn all tty ports on|
|F	|4	|4	|turn ROS on|

## Repository Folders
Para el proyecto usamos algunas librerias.
### PIC
* Timer.c

#### Timer.c
Esta librería funciona como un reloj fijo.
### Python
Los siguientes archivos son nodos los cuales publican su información por medio de tópicos con la ayuda de la librería ROS
* Firmware.py
* Monitoring.py
* Resources.py
* Sim_vn300.py
* Prueba_serial_dspic.py

#### Sim_vn300.py
Es un nodo que simula la ejecución del vn_300 publicado la información mediante un tópico con su mismo nombre   

### DSPIC
* I2C_DIR
* Max17055.bak
* Max17055.cpp
* Max17055.h
* NOTAS.C
* Nuc_interface.h
* TONOS.C
* Hadware_actions.h
* Ports.h
* SerialProtocol.h
* ws2815b.C

####  I2C_DIR
La comunicación con algunos sensores se hace mediante el protocolo I2C y este  se encuentra en un pin específico que se encuentra en la hoja de datos del producto, así mismo  el puerto del micro de I2C debe ir a un el mux pues se necesita enviar y recibir datos de varios sensores.
#### Max17055.h
Esta librería se usa para tomar la lectura del estado actual de la batería y además hacer una copia de respaldo de las mediciones.Esta librería se usa para tomar la lectura del estado actual de la batería y además hacer una copia de respaldo de las mediciones, de igual manera esta librería se basó en Max17055.bank y Max17055.cpp. 
#### Notas.C
Esta librería se usa para definir el tiempo de una nota usada por el Buzzer en el sistema.
#### Nuc_interface.h
Esta librería se usa para apagar la NUC y la batería de 12v.
#### Tonos.C
En esta librería usamos las notas típicas y a su vez cada nota posee 4 frecuencias distintas separadas por octavas.
#### Hadware_actions.h
Esta librería se usa para detectar un error en los sensores e informar mediante el buzzer o mediante el led RGB, además esta librería tiene un sonido especifico y un color especifico por el error correspondiente.
#### Ports.h
Esta librería se usa para definir  a que pin está conectado los periféricos.
#### SerialProtocol.h
Esta librería es usada para la comunicación del micro con la NUC la cual fue explicada anteriormente.
#### ws2815b.C
Esta librería es usada para el funcionamiento del LED ws2815b escogiendo un color dentro del espectro RGB.

### Authors.








