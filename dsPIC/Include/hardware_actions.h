#include <stdlib.h>

#ifndef hardware_actions
void system_info(char data){
	switch (data){
		case 0x0:
			// Error
			generate_tone(NOTA_si[2],corchea);
			generate_tone(NOTA_si[2],semicorchea);
			break;
		case 0x1:
			//
			break;
		case 0x2:
			//
			break;
		case 0x3:
			//
			break;
		case 0x4:
			//
			break;
		case 0x5:
			//
			break;
		case 0x6:
			//
			break;
		case 0x7:
			//
			break;
		case 0x8:
			//
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
void peripherals_info(char data){
	switch (data){
		case 0x0:
			// Error
			generate_tone(NOTA_si[2],corchea);
			generate_tone(NOTA_si[2],semicorchea);
			break;
		case 0x1:
			// xx no connected
			generate_tone(NOTA_si[2],negra);
			generate_tone(NOTA_si[2],corchea);
			break;
		case 0x2:
			// xx starting
			generate_tone(NOTA_do[2],corchea);
			generate_tone(NOTA_do[2],semicorchea);
			break;
		case 0x3:
			// vn300 < 25%
			generate_tone(NOTA_mi[2],corchea);
			generate_tone(NOTA_mi[2],semicorchea);
			break;
		case 0x4:
			// 25% < vn300 < 50%
			generate_tone(NOTA_mi[2],negra);
			generate_tone(NOTA_mi[2],corchea);
			break;
		case 0x5:
			// 50% < vn300 < 75%
			generate_tone(NOTA_mi[2],blanca);
			generate_tone(NOTA_mi[2],negra);
			break;
		case 0x6:
			// vn300 > 75%
			generate_tone(NOTA_mi[2],blanca);
			generate_tone(NOTA_mi[2],blanca);
			break;
		case 0x7:
			// xx working
			generate_tone(NOTA_sol[2],corchea);
			generate_tone(NOTA_sol[2],semicorchea);
			break;
		case 0x8:
			//
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
/********************************************/
// Hardware actions
/********************************************/
void H_actions(char dato1, char dato2){
	if (dato1 == 0x00){
		system_info(dato2);
	}
	else if ((dato1>0x00)&&(dato1<=0x0f)){
		peripherals_info(dato2);
	}
	else{
		generate_tone(NOTA_si[2],corchea);
		generate_tone(NOTA_si[2],semicorchea);
	}
}
#define hardware_actions

#endif