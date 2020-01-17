import time
import serial

# configure the serial connections
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    timeout = 0,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

flag = False
cont = 0
ser.close()
time.sleep(5)
ser.open()
#ser.isOpen()
print (ser.portstr)

while True:
        if flag:
            print("Envió\n")
            ser.write("a\r\n")
        print (ser.readline())
        time.sleep(1)
        cont = cont+1
        if cont == 10:
            cont = 0
            flag = not(flag)