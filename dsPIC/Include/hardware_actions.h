#include <stdlib.h>
int cont_comm = 0;
#ifndef hardware_actions
/***************************************/
//			L2 L3 L4 L1 button
/***************************************/
void action(){
	if (f_error){
		generate_tone(NOTA_si[2],corchea);
		generate_tone(NOTA_do[2],semicorchea);
		f_error = 0;
	}
	if (!f_conn){
		generate_tone(NOTA_si[2],corchea);
		generate_tone(NOTA_si[2],semicorchea);
		f_conn = 1;
	}
	if (f_conSta>0){
		generate_tone(NOTA_mi[f_conSta-1],corchea);
		generate_tone(NOTA_mi[f_conSta-1],semicorchea);
	}
	if (f_satar==1){
		opening2();
	}
	else if (f_satar>1){
		f_satar = 20;
	}
	if (f_begin){
		generate_tone(NOTA_do[2],corchea);
		generate_tone(NOTA_do[2],semicorchea);
		f_begin = 0;
	}
	if(RAM_error == 2){
		generate_tone(NOTA_sol[2],corchea);
		generate_tone(NOTA_sol[2],corchea);
	}
	if(HDD_error == 2){
		generate_tone(NOTA_la[2],corchea);
		generate_tone(NOTA_do[2],semicorchea);
		generate_tone(NOTA_la[2],corchea);
	}
	if(HDD_error == 3){
		generate_tone(NOTA_si[3],corchea);
		generate_tone(NOTA_si[3],corchea);
		generate_tone(NOTA_si[3],corchea);
	}
}

void system_info(char dta, char data){
	switch (data){
		case 0x0:
			// Error
			f_error = 1;
			R1 = 0; G1 = 0; B1 = 0; R2 = 0; G2 = 0; B2 = 0;
			R3 = 0; G3 = 0; B3 = 0; R4 = 0; G4 = 0; B4 = 0;
			break;
		case 0x1:
			if(dta == 0x0a){
				//RAM Alert 1
				RAM_error = 1;
				R3 = 255;
				G3 = 64;
				B3 = 64;
			}
			else{
				// Turn_on 24
				output_high(EN24);
			}
			break;
		case 0x2:
			if (dta == 0x0a){
				//RAM Alert 2
				RAM_error = 2;
				R3 = 255;
				G3 = 0;
				B3 = 0;
			}
			else{
				//Turn-off 12V
				output_low(EN12);
			}
			break;
		case 0x3:
			if (dta == 0x0a){
			}
			else{
				//Turn-off 24V
				output_low(EN24);
			}
			break;
		case 0x4:
			//
			break;
		case 0x5:
			//
			break;
		case 0x6:
			if (dta == 0x0a){
				//ROM Alert 1
				HDD_error = 1;
				R3 = 64;
				G3 = 133;
				B3 = 255;
			}
			else{
			}
			break;
		case 0x7:
			if (dta == 0x0a){
				//ROM Alert 2
				HDD_error = 2;
				R3 = 64;
				G3 = 64;
				B3 = 255;
			}
			else{
			}
			break;
		case 0x8:
			if (dta == 0x0a){
				//ROM Alert 3
				HDD_error = 3;
				R3 = 0;
				G3 = 0;
				B3 = 255;
			}
			else{
			}
			break;
		case 0x9:
			//
			break;
		case 0xa:
			//
			break;
		case 0xb:
			//
			break;
		case 0xc:
			//
			break;
		case 0xd:
			//
			break;
		case 0xe:
			//
			break;
		case 0xf:
			//
			break;
		default:
			//
			break;
	}
}
void peripherals_info(char dta, char data){
	switch (data){
		case 0x0:
			// Error
			f_error = 1;
			R1 = 0; G1 = 0; B1 = 0; R2 = 0; G2 = 0; B2 = 0;
			R3 = 0; G3 = 0; B3 = 0; R4 = 0; G4 = 0; B4 = 0;
			break;
		case 0x01:
			// xx no connected
			//f_conn = 0;
			switch (dta){
				case 1:
					R1 = 240;
					G1 = 0;
					B1 = 0;
					break;
				case 2:
					R2 = 240;
					G2 = 0;
					B2 = 0;
					break;
			}
			break;
		case 0x02:
			// xx starting
			//f_begin = 1;
			switch (dta){
				case 1:
					R1 = 240;
					G1 = 128;
					B1 = 0;
					break;
				case 2:
					R2 = 240;
					G2 = 128;
					B2 = 0;
					break;
			}
			break;
		case 0x03:
			// vn300 < 25%
			f_conSta = 1;
			R1 = 50;
			G1 = 0;
			B1 = 240;
			break;
		case 0x04:
			// 25% < vn300 < 50%
			f_conSta = 2;
			R1 = 50;
			G1 = 80;
			B1 = 160;
			break;
		case 0x05:
			// 50% < vn300 < 75%
			f_conSta = 3;
			R1 = 50;
			G1 = 160;
			B1 = 80;
			break;
		case 0x06:
			// vn300 > 75%
			f_conSta = 4;
			R1 = 50;
			G1 = 240;
			B1 = 0;
			break;
		case 0x07:
			// xx working
			f_satar ++;
			switch (dta){
				case 1:
					R1 = 0;
					G1 = 240;
					B1 = 0;
					break;
				case 2:
					R1 = 0;
					G1 = 240;
					B1 = 0;
					break;
			}
			break;
		case 0x08:
			//
			break;
		case 0x09:
			//
			break;
		case 0x0a:
			//
			break;
		case 0x0b:
			//
			break;
		case 0x0c:
			// u_T1
			if(dta==4){
				cycles = 0;
				R4 = 13;
				G4 = 0;
				B4 = 125;
			}
			break;
		case 0x0d:
			// u_T2
			if(dta==4){
				cycles = 3;
				R4 = 113;
				G4 = 0;
				B4 = 125;
			}
			break;
		case 0x0e:
			// u_T3
			if(dta==4){
				cycles = 6;
				R4 = 255;
				G4 = 128;
				B4 = 0;
			}
			break;
		case 0x0f:
			// u_T4
			if(dta==4){
				cycles = 9;
				R4 = 250;
				G4 = 0;
				B4 = 0;
			}
			break;
		default:
			//
			break;
	}
}
/********************************************/
// Hardware actions
/********************************************/
void H_actions(char dato1, char dato2){
	if (cont_comm == 5){
		if ((dato1 == 0x00)||(dato1 > 0x09)){
			system_info(dato1,dato2);
		}
		else if ((dato1>0x00)&&(dato1<=0x09)){
			peripherals_info(dato1,dato2);
		}
		else{
			f_error = 1;
		}
		
	}
	cont_comm ++;
	if (cont_comm == 6)
		cont_comm = 0;
}
#define hardware_actions

#endif