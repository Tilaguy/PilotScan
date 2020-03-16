#include <stdlib.h>
#include <Include\hardware_actions.h>

//************************************************
/*
Command		meaning
	0		reserved
	1		current source 5
	2		current source 12
	3		current source 24
	4		current source battery
	5		Voltage source 5
	6		Voltage source 12
	7		Voltage source 24
	8		Voltage source Battery
	9		Temperature LiDAR
	A		Temperature dsPIC
	B		Temperature DC
	C		Temperature xx
	D		Hight
*/
//************************************************
char NUC_state[2];

#ifndef serialProtocol

/********************************************/
// data2hex function
/********************************************/
long data2Hex(float data, char command){
	char data1 = 0;
	char data2 = 0;
	int checksum = 0;
	long data_hex = 0x00;
	
	char data_int = 0;
	int p1 = 0;
	int p2 = 0;
	
	if (data>=16){
		p1 = (int)(data/16.0);
		p2 = ((int)(data))%16;
		data = p1+(p2/100.0);
		checksum = 5;
	}
		
	if (command != 0x0){
		// data1
		/********************************************/
		data_int = (char)(data);
		if (data_int < 16)
			data1 = data_int%16;
		else
			data1 = 0;
		// data2
		/********************************************/
		data_int = ((int)(data*100.0))%100;
		if (data_int < 16)
			data2 = data_int%16;
		else{
			data2 = data_int/10;
		}
		// checksum
		/********************************************/
		checksum += command+data1+data2;
		// data_hex
		/********************************************/
		data_hex |= command;
		data_hex <<= 4;
		data_hex |= data1;
		data_hex <<= 4;
		data_hex |= data2;
		data_hex <<= 8;
		data_hex |= checksum;
	}
	else{
		data_hex = 0;
	}
	return data_hex;
}

/********************************************/
// hex2data function
/********************************************/
void Hex2data(char *data[], int n){
	char dato1 = 0;
	char dato2 = 0;
	char checksum = 0;
	char data_aux[5];
	unsigned int data_int = 0;
	unsigned int i;
	//printf ("Recibido_dato = %s\n", data);
	if (data[0]=='$'){
		//printf ("Recibido2_dato = %s\n", data);
		for (i=1; i<=(n-1); i++){
			data_aux[i-1] = data[i];
		}
		//printf ("Recibido_dato_aux = %s\n", data_aux);
		data_int = atoi(data_aux);
		//printf ("Recibido_dato = %d\n", data_int);
		dato1 = 0x0F&(data_int>>12);
		//printf ("Recibido_dato1 = %x\n", dato1);
		dato2 = 0x0F&(data_int>>8);
		//printf ("Recibido_dato2 = %x\n", dato2);
		checksum = 0xFF&data_int;
		if ((dato1+dato2)!=checksum){
			dato1 = 0;
			dato2 = 0;
		}
		NUC_state[0] = dato1;
		NUC_state[1] = dato2;
//		if (f_perPass!=dato1){
//			f_perPass = dato1;
//			f_satar = 0;
//		}
	}
}
#define serialProtocol

#endif