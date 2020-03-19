## PILOT SCAN
---
En construccion...
---
### 1. Descripción

En este repositorio se encuentran alojados los algoritmos necesarios para elaborar una interfaz de comunicación codificada con capacidad de detección de errores, durante el proceso de envío. Esta interfaz hace parte del sistema titulado **PilotScan\***, el cual consta de un sistema central de procesamiento y un sistema de respaldo que monitora de forma continua, el estado del sistema tanto a nivel hardware como software, además tiene la capacidad de realizar acciones indicadas por sistema central, sobre los diferentes módulos que conforman el sistema.

Para el sistema central de procesamiento, se usa una **Intel®️ NUC Board** con Linux 16.04 server. Para el sistema de respaldo se emplea un **dsPIC 30F4011**, el cual conecta diferentes sensores analógicos y digitales, tiene la capacidad de habilitar y deshabilitar fuentes reguladas de *12 V* y *24 V*, además de emitir mensajes al usuario a través de una bocina y leds RGB programables.

**\*** La información detallada del sistema se encuentra alojada en el repositorio: \ link \

---
## 2. Repository organization
Este repositorio se encuentra organizado de la siguiente forma:

### 2.1. PIC
* *Timer.c*:  Este archivo genera un reloj a frecuencia constante en un microcontrolador **PIC 16f506**, el cual sirve como base de tiempo para garantizar que el sistema de firmware está en funcionamiento.
### 2.2. Python
Estos archivos son nodos para ROS, los cuales interactúan entre sí por medio de tópicos para el monitoreo, procesamiento y acción sobre los diferentes módulos que conforman el sistema **PilotScan**.

* *Firmware.py*:  Nodo encargado de la recepción y transmisión serial con el sistema de respaldo.

* *Monitoring.py*:  Nodo encargado del procesamiento, codificación y decodificación de la información mediante protocolos diseñados para cada caso específico.

* *Resources.py*:  Nodo que lee la información del estado del sistema y la publica por medio de tópicos separados como el estado de memoria, la temperatura de los núcleos y entre otros.

### 2.3. dsPIC
#### 2.3.1. Include

* *ports.h*:  Librería para hacer asignaciones de pines según su uso y declaración de variables globales.

* *NOTAS.C*:  Librería para definir el tiempo de una nota usada por el Buzzer en el sistema.

* *TONOS.C*:  Librería donde se definen las notas musicales separado por octavas en 4 grupos de frecuencias diferentes.

* *SerialProtocol.h*:  Librería encargada de la codificación y decodificación de la información mediante protocolos diseñados para cada caso específico.

* *Hadware_actions.h*:  Librería usada para generar acciones o notificaciones del estado del sistema mediante el buzzer o los LEDs RGB.

* *Nuc_interface.h*:  Librería usada para encender y apagar el sistema de cómputo central.

* *I2C_DIR*:  Libreria que contiene las definiciones de direcciones I2C para la comunicación con algunos sensores, las funciones correspondientes para establecer dicha comunicación.

#### 2.3.2. Main
En el archivo main.c se hace uso de las librerías mencionadas anteriormente, se realiza la configuración de los diferentes periféricos de microcontrolador como modulo ADC, I2C, RS232, entre otros. Adicionalmente, se realiza la configuración y activación de interrupciones.

---

## 3. Comunicación serial **computador-dsPIC**
El protocolo que se usa para la comunicación entre el microcontrolador y el computador, genera un número que codifica la información en hexadecimal, esta codificación depende de quién es emisor del mensaje, esta codificación se explica más detalladamente a continuación. Además, el protocolo cuenta con un Byte de inicio (*'$'*) que indica el comienzo del mensaje y un salto de línea (*'\n'*) que informa el final. En cualquier caso, si los Bytes de información toman los valores de 0, significa un error en la codificación.

### 3.1. Protocolo de envió desde la Intel® NUC Board
Este protocolo se construye a partir de una tabla de valores constantes, los cuales indican el estado del sistema en diferentes ámbitos tales como: monitoreo y control de las fuentes, la comunicación de problemas de ejecución y otros requerimientos necesarios para el correcto funcionamiento del sistema. Dicho protocolo consta de dos Byte, los cuales codifican la información.

El primer Byte (**data1**) indica el origen de la información (VN-300, Lidar, estado del sistema, etc) de la cual se está dando a conocer su estado. El segundo Byte (**data2**) informa el estado y da idea de cómo debe proceder el microcontrolador. Los dos Bytes restantes corresponden al checksum, quien funciona como sistema de detección de errores en el proceso de comunicación, pues dichos Bytes deben corresponden a la suma de los dos primeros (**dato1+dato2**).

Cada mensaje es interpretado por el microcontrolador quien efectúa algún tipo de acción, ya sea realizando un encendido o apagado de algún elemento, activando alertas auditivas o alertas visuales a través de LEDs RGB.

* **P. ej.** Si la *temperatura media de los núcleos del sistema de cómputo* esta entre 35 °C y 40 °C, en microcontrolador debe *encender los ventiladores* en cierta forma particular.
  * Mensaje enviado:
  ~~~
  data1 =      0x4
  data2 =      0xE
  checksum =   0x12
  mensaje =    '$19986\n'
  ~~~
  * Acción tomada por el microcontrolador:
  ~~~
  - Encendido de ventidador ( PWM ~ 60% )
  - LED RGB 4 ([R,G,B] = [25,128,0])
  ~~~
#### Tabla 1. Mensajes del sistema.

data 1 | data 2 | message | meaning
-- | -- | -- | -- 
0 | 0 |         |Reserve
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

#### Tabla 2. Mensajes del estado del VN300.
data 1 | data 2 | message | meaning | R | G | B |LED
-- | -- | -- | -- | -- | -- | -- |--
1 | 0 |         |Reserve|0|0|0|L1
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

#### Tabla 3. Mensajes del estado del LiDAR M8.
data 1 | data 2 | message | meaning | R | G | B |LED
-- | -- | -- | -- | -- | -- | -- | --
2 | 0 |         |Reserve|0|0|0|L2
2 | 1 | M8-NC |	M8 No Ping|240	|0|0|L2
2 | 2 | M8-Start |M8 Starting|240|128|0|L2
2 | 3 |
2 | 4 |
2 | 5 |
2 | 6 |
2 | 7 |M8-Work | M8 Working|0|240|0 |L2
2 | 8 |
2 | 9 |
2 | A |
2 | B |
2 | C |
2 | D |
2 | E |
2 | F |
#### Tabla 4. Mensajes del estado de la camara.
data 1 | data 2 | message | meaning
-- | -- | -- | --
3 | 0 |         |Reserve
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
#### Tabla 5. Mensajes del control Fuzzy para temperatura.
data 1 | data 2 | message | meaning | R | G | B|LED
-- | -- | -- | -- | -- | -- | -- |--
3 | 0 |  |Reserve|0|0|0|L4
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
3 | C |FUZZ-T1|>25°|13	|0|	125|L4
3 | D |FUZZ-T2|>30°|113|	0|	125|L4
3 | E |FUZZ-T3|>35°|255|	128|	0|L4
3 | F |FUZZ-T4|>40°|250|0|	0|L4
#### Tabla 6. Mensajes de error de memoria.
data 1 | data 2 | message | meaning | R | G | B |LED
-- | -- | -- | -- | -- | -- | -- | --
A | 0 |  |Reserve|0|0|0|L3
A | 1 | memo-RAM_E1 |RAM alert1|255|64|64|L3
A | 2 | memo-RAM_E2 |RAM alert2|255|0|0|L3
A | 3 |
A | 4 |
A | 5 |
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
### 3.2. Protocolo de envió desde el dsPIC
Este protocolo se construye a partir de una tabla de valores constantes y los datos numéricos codificados en hexadecimal, que informan al computador sobre las variables medidas por el microcontrolador. Dicho protocolo consta de tres Bytes que codifican la información, los cuales son enviados al computador para ponerlo en conocimiento de los valores numéricos de las variables fundamentales para el funcionamiento de las tarjetas.

El primer Byte corresponde al tipo de información (**command**) como corrientes, voltajes, etc, y su origen. Los siguientes dos Bytes son la información numérica codificada (**data1**, **data2**), la cual puede ser entera o flotante. Adicionalmente, existen dos Bytes corresponden al checksum, el cual permite verificar la información transmitida como protocolo de detección de errores y además permite conocer si el dato numérico enviado es un entero con rango [0, 255] (**command+data1+data2+0x05**), o un flotante con una cifra decimal de precisión (**command+data1+data2**).


* **P. ej.** La *corriente proveniente de la fuente de 5 V* medida por el sensor es de *0.45 A*, a su vez *el altímetro* detecta una altura de *64 m*.
  * Mensaje 1 enviado:
  ~~~
  Command =    0x1
  data1 =      0x0
  data2 =      0x4
  checksum =   0x05
  mensaje =    '$66565\n'
  ~~~
  * Mensaje 2 enviado:
  ~~~
  Command =    0xD
  data1 =      0x4
  data2 =      0x0
  checksum =   0x16
  mensaje =    '$868374\n'
  ~~~
#### Tabla 7. Variables medidas codificadas.
   
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

#### Tabla 8. Estado de los módulos del sistema.
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

---

### 4. Software requirements

#### 4.1. System_monitor Installation
Insatalación del System_monitor node para ROS: (https://github.com/RobotnikAutomation/system_monitor)

Dentro de la carpeta src del workspace, se debe descargar el *system_monitor* usando la siguiente instrucción:
~~~
$ git clone https://github.com/RobotnikAutomation/system_monitor
~~~
Es necesario instalar algunas dependencias adicionales para su ejecución,
~~~
$ sudo apt-get install sysstat ifstat ntpdate
~~~
Luego, se compila en el workspace y se asigna el directorio *devel*,
~~~
$ catkin_make
$ source devel/setup.bash
~~~
Por último, para lanzar el nodo se usa la instrucción:
~~~
$ roslaunch system_monitor system_monitor.launch
~~~

---
### 5. Authors.


