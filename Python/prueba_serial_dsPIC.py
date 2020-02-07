import time
import serial

# Configure the serial connexions 
ser = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 9600,
	timeout = 0,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS
)

flag = False
flag2 = False
cont = 0
data1 = 0
data2 = 0
ser.close()
ser.open()
print (ser.portstr)

def data2Hex(message):
	message2 = message.split('-')
	if message2[0]=="sys":
		sw1 = {
			"sys":		'0'
		}
		sw2 = {
			"on_24":	'1',
			"off_12":	'2',
			"mem_e":	'3',
			"on_m8":	'4',
			"on_tty":	'5',
		}
	else:
		sw1 = {
			"vn300":	'1',
			"m8":		'2',
			"cam":		'3'
		}
		sw2 = {
			"NC":		'1',
			"start":	'2',
			"<25":		'3',
			"<50":		'4',
			"<75":		'5',
			">75":		'6',
			"work":		'7'
		}
	sw3 = {
		0:	'0',
		1:	'1',
		2:	'2',
		3:	'3',
		4:	'4',
		5:	'5',
		6:	'6',
		7:	'7',
		8:	'8',
		9:	'9',
		10:	'a',
		11:	'b',
		12:	'c',
		13:	'd',
		14:	'e',
		15:	'f'
	}
	data1 = sw1.get(message[0],'0')
	data2 = sw2.get(message[1],'0')
	checksum_int = int(data1,16) + int(data2,16)
	checksum1 = sw3.get(checksum_int/16,'0')
	checksum2 = sw3.get(checksum__int%16,'0')
	string = data1+data2+checksum1+chcksum2
	return int(string,16)

while True:
	string = "$"
	time.sleep(0.1)
	if flag:
		if not flag2:
			data1 = 0x0
			data2 = 0x1
			print data1,data2
			checksum = data1+data2
			
			print checksum
			print "$1799"
		ser.write("$1799\n")
		cont = 0
		flag = False
	else:
		a = ser.readline()
		if len(a)>0:
			print a
			cont = cont+1
			if cont == 10:
				flag = True
