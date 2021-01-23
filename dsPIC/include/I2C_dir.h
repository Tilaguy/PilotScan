//#include <MAX17055.cpp>

int16 Ibat, avgI, avgV, Vbat;
int1 select_ch = 1;
/********************************************/
// I2C directions
/********************************************/
/******* MUX I2C ********/
#define mux_i2c		0xE0 		// Direction of I2C mux
#define mux_ch0		0x01		// Enable ch0 of mux Temp
#define mux_ch1		0x02		// Enable ch1 of mux
#define mux_ch2		0x04		// Enable ch2 of mux
#define mux_ch3		0x08		// Enable ch3 of mux
/******* Temp Sensors ********/
#define T_dsPic		0x90		// Read dsPIC temperature
#define T_a			0x94		// Read ambient temperature
#define T_power		0x98		// Read Power_PCB temperature
#define T_LiDAR		0x9C		// Read LiDAR temperature
#define T_pnt_R		0x00		// Temperature register (only read)
#define T_pnt_conf	0x01		// Configuration register
#define T_pnt_TL	0x02		// Temperature alert low
#define T_pnt_TH	0x03		// Temperature alert high
/******* Battery ********/
#define batt_slave	0x6C		// Slave address
#define m_current	0x0A		// Current and avgcurrent registers
#define m_voltage	0x19		// Voltage and avgvoltage registers
/******* Light Sensors ********/

/*
Write, Read  and block			0x000	0x0FF
								0x180	0x1FF
one only word					0x100	0x17F
specific registers (page 45)				
informacion para determinar si el paquete de celdas esta vacias			0x1A0	
			0x1A1	
			0x1A2	
			0x1A3	
numero total de ciclos completos			0x1A4	
				
capacidad por celda			0x1A5	
Indicador de voltaje 			0xA6	
			0xA7	
Corritente tipica cuando la celda esta vacia 			0xA8	
capacidad de la celda en condiciones actuales 			0xA9	
voltaje y temperatura promedio			0xAA	
Máxima y mínima corriente, voltaje y temperatura 			0xAB	
			0xAC	
			0xAD	
estado de la carga actual			0xAE	
tiempo total trascurrido 			0xAF	
*/

void I2C_channel(BYTE mode, int ch){
	//if (select_ch){
		// mode -> 1: read; 0: write
		i2c_start(); 					// Star
		i2c_write(mux_i2c|mode);		// Slave direction and mode
		i2c_write(ch); 					// Channel selection
		i2c_stop(); 					// End comunication
		delay_us(15);
		select_ch = 0;
	//}
}

int Temperature(int addr){
	int T_h, T_l, T_Byte;
	// mode -> 1: read; 0: write
//	generate_tone(NOTA_DOS[2], corchea);
	i2c_start(); 			//Star
	i2c_write(addr|0);		//Direction
	i2c_write(T_pnt_R);
	i2c_start(); 			//Restar
	i2c_write(addr|1);		//Direction
	T_h = i2c_read();
	T_l = i2c_read();
	i2c_stop(); 			//Finaliza comunicación
	T_Byte = (T_h<<8)|T_l;
	printf ("Th-%d\n",T_h);
	printf ("Tl-%d\n",T_l);
	return T_Byte;
}

//void Temperature_config(){
//	i2c_start(); 				// Star
//	i2c_write(addr|1);			// Direction
//	i2c_write(T_pnt_R);			// Pointer register
//	i2c_write(addr|mode);		// Byte 1
//	i2c_write(addr|mode);		// Byte 2
//	i2c_stop(); 				//Finaliza comunicación
//}

void current_read(){
	int I_h, I_l, avgI_h, avgI_l;
	int1 state;
	i2c_start(); 				// Star
	i2c_start(); 				// Star
	Error:
	state = i2c_write(batt_slave|0);
//	if(state==1)	// Reg direction | wite
//		generate_tone(NOTA_DOS[2], corchea);
		//goto Error;
	state = i2c_write(m_current);
//	if(state==1)		// Pointer register
//		generate_tone(NOTA_DOS[2], corchea);
		//goto Error;
	i2c_start(); 				// Restar
	state = i2c_write(batt_slave|1);
//	if(state==1)	// Reg direction | read
//		generate_tone(NOTA_DOS[2], corchea);
		//goto Error;
	I_h = i2c_read();
	I_l = i2c_read();
	avgI_h = i2c_read();
	avgI_l = i2c_read();
	i2c_stop(); 				//Finaliza comunicación
	Ibat = (I_h<<8)|I_l;
	avgI = (avgI_h<<8)|avgI_l;
//	printf ("Ih-%d\n",I_h);
//	printf ("Il-%d\n",I_l);
}

void voltage_read(){
	int V_h, V_l, avgV_h, avgV_l;
	i2c_start(); 				// Star
	i2c_write(batt_slave|0);	// Slave direction | wite
	i2c_write(m_voltage);		// Pointer register
	i2c_start(); 				// Restar
	i2c_write(batt_slave|1);	// Slave direction | read
	V_h = i2c_read();
	V_l = i2c_read();
	avgV_h = i2c_read();
	avgV_l = i2c_read();
	i2c_stop(); 				//Finaliza comunicación
	Vbat = (V_h<<8)|V_l;
	avgV = (avgV_h<<8)|avgV_l;
//	printf ("Vh-%d\n",V_h);
//	printf ("Vl-%d\n",V_l);
}