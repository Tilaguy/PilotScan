
#include <xc.h>
//#device ADC=12
#define OSC_INTERNAL
//#use delay (clock = 120000000)
//#fuses FRC_PLL16,NOPROTECT,NOWDT,NOPUT,MCLR

//#use RS232(BAUD=9600,BITS=8,PARITY=N,XMIT=PIN_C13,RCV=PIN_C14,TIMEOUT=10)// UART
//#use i2c(Master,sda=PIN_F2,scl=PIN_F3)// I2C

/********************************************/
// Import Libraies
/********************************************/
#include "ports.h"
#include <Include\NOTAS.c>
#include <Include\TONOS.c>
#include <Include\serialProtocol.h>
#include <Include\NUC_interface.h>
#include <Include\I2C_dir.h>

/********************************************/
// Global Variables
/********************************************/

int1 aux_binary = 1;
int1 flag_info = 0;
int1 shut_down = 0;
int cont_tm4 = 0;
char cont_tm5 = 0;
int16 I5, I12, I24, m24V, m12V, m05V, mVbat;
char buffer[6];



const float S2I = 1.25*3.0/4095.0;	// Sensor of current
const float S24 = 11.99*3.0/4095.0;	// Sensor of 24 V
const float S12 = 6.19*3.0/4095.0;	// Sensor of 12 V
const float S05 = 2.35*3.0/4095.0;	// Sensor of 05 V
const float Sbat = 4.33*3.0/4095.0;	// Sensor of batery voltage

/********************************************/
// General configuration
/********************************************/

void ADC_setup(){
	setup_adc_ports(sAN0 | sAN1 | sAN2 | sAN3 | sAN4 | sAN5 | sAN6);
	setup_adc(ADC_CLOCK_INTERNAL);
}

void INT_setup(){
	ENABLE_INTERRUPTS(INTR_GLOBAL);
	EXT_INT_EDGE(L_TO_H);
	CLEAR_INTERRUPT(INT_EXT0);
	CLEAR_INTERRUPT(INT_RDA);
}
/********************************************/
// General Functions
/********************************************/

void linea2(){
	generate_tone(NOTA_MI[2],negra);
}

int16 Read_ADC_ports(int ch){
	SET_ADC_CHANNEL(ch);
	delay_us(10);
	return READ_ADC();
}
// Declaration of time constans
// Practical estimation of timing waveforms
const int TH0 = 5;//0.3us
const int TH1 = 16;//0.6us
const int TL0 = 16;//0.9us
const int TL1 = 7;//0.6us

// Color  chage  Detection
void RBG(int R,int  G,int B){
	int i;
	// Green value
	for(i = 0;i<8;i++){
		output_high(LED_RGB);
		if ((G>>7)&0x01){
			delay_cycles(TH1);
			output_low(LED_RGB);
			delay_cycles(TL1);
		}
		else{
			delay_cycles(TH0);
			output_low(LED_RGB);
			delay_cycles(TL0);
		}
		G<<=1;
	}
	// Red value
	for(i = 0;i<8;i++){
		output_high(LED_RGB);
		if ((R>>7)&0x01){
			delay_cycles(TH1);
			output_low(LED_RGB);
			delay_cycles(TL1);
		}
		else{
			delay_cycles(TH0);
			output_low(LED_RGB);
			delay_cycles(TL0);
		}
		R<<=1;
	}
	// Blue value
	for(i = 0;i<8;i++){
		output_high(LED_RGB);
		if ((B>>7)&0x01){
			delay_cycles(TH1);
			output_low(LED_RGB);
			delay_cycles(TL1);
		}
		else{
			delay_cycles(TH0);
			output_low(LED_RGB);
			delay_cycles(TL0);
		}
		B<<=1;
	}
}

void send_serial(long data){
	printf ("$%ld\n",data);
}

/********************************************/
// Interruptions
/********************************************/
#int_EXT0
void  EXT0_isr(void){
	CLEAR_INTERRUPT(int_EXT0);
	aux_binary = !aux_binary;
//	OUTPUT_BIT(LED1,aux_binary);
}

#int_RDA
void RDA_isr(void){
	disable_interrupts(int_rda);
    unsigned int i = 0;
    char inp;
    inp = getc();
    //putc(inp);
    while(inp != '\n'){
        buffer[i] = inp;
        inp = getc();
        //putc(inp);
        i++;
    }
    int n = sizeof(buffer);
    Hex2data(buffer,n);
	ENABLE_INTERRUPTS(int_rda);
}

#int_TIMER4
void  TIMER4_isr(void){
	disable_interrupts(INT_TIMER4);
	if (cont_tm4==50){
		if (INPUT(Cap_bot)){
			enable_interrupts(INT_TIMER4);
			//generate_tone(NOTA_si[2],corchea);
			output_high(EN_ANA);
			output_high(EN_VBAT);

			//time_off = 0;
//			if (INPUT(NUC_LED)){
//				sw_NUC(); 			// Turn on NUC
//				delay_ms(120000);
//			}else{
//				/********************************************/
//				// Main Program
//				/********************************************/
//				H_actions(0x04, 0x0d);
				H_actions(NUC_state[0],NUC_state[1]);

				send_serial(data2Hex(I5*S2I, 0x01));
				send_serial(data2Hex(I12*S2I, 0x02));
				send_serial(data2Hex(I24*S2I, 0x03));
				send_serial(data2Hex(m05V*S05, 0x05));
				send_serial(data2Hex(m12V*S12, 0x06));
				send_serial(data2Hex(m24V*S24, 0x07));
				send_serial(data2Hex(mVbat*Sbat, 0x08));

				shut_down = 0;
				output_low(EN_ANA);
				output_low(EN_VBAT);
				flag_info = 1;

				RBG(R1,G1,B1);
				RBG(R2,G2,B2);
				RBG(R3,G3,B3);
				RBG(R4,G4,B4);
//			}
		}else{
			if (!shut_down){
				Ending1();
				output_low(EN_VBAT);
				shutdown_NUC();
				output_low(EN12);
				output_low(EN24);
				output_low(EN_ANA);
				shut_down = 1;
			}
		}
		cont_tm4 = 0;
	}
	else{
		cont_tm4++;
	}
	set_timer4(0);
	enable_interrupts(INT_TIMER4);
}

#int_TIMER5
void  TIMER5_isr(void){
	if (cont_tm5 < cycles){
		output_high(FAN_A);
		output_high(FAN_B);
	}
	else{
		output_low(FAN_A);
		output_low(FAN_B);
	}
	cont_tm5 ++;
	if (cont_tm5 == 10)
		cont_tm5 = 0;
}

/********************************************/
// Main Function
/********************************************/
void main(){
	setup();
	output_low(EN12);
	output_low(EN24);
	output_low(EN_ANA);
	output_high(NUC_ON_OFF);
	ADC_setup();
	INT_setup();
	setup_timer4(TMR_INTERNAL |TMR_DIV_BY_256 ,1550);
	setup_timer5(TMR_INTERNAL |TMR_DIV_BY_8 ,453);

	delay_ms(300);


//	int data_in = 0;
//	int n = 0;
	delay_ms(500);
	output_high(EN12);
	output_high(EN24);
	delay_ms(500);
	INPUT(Cap_bot);


	/***************************************/
	//			L2 L3 L4 L1 button
	/***************************************/
	int cont_RGB = 0;
	R1 = 0; G1 = 250; B1 = 0; R2 = 0; G2 = 250; B2 = 0;
	R3 = 0; G3 = 250; B3 = 0; R4 = 0; G4 = 250; B4 = 0;
	do{
		if (cont_RGB < 250){
			RBG(0,0,0);
			RBG(255,128,0);
			RBG(0,0,0);
			RBG(0,0,0);
		}else if(cont_RGB < 500){
			RBG(0,0,0);
			RBG(0,250,0);
			RBG(255,128,0);
			RBG(0,0,0);
		}else if(cont_RGB < 750){
			RBG(0,0,0);
			RBG(0,250,0);
			RBG(0,250,0);
			RBG(255,128,0);
		}else{
			RBG(255,128,0);
			RBG(0,250,0);
			RBG(0,250,0);
			RBG(0,250,0);
		}
		delay_ms(1);
		cont_RGB++;
	}while(cont_RGB<2000);
	RBG(R1,G1,B1);
	RBG(R2,G2,B2);
	RBG(R3,G3,B3);
	RBG(R4,G4,B4);

	opening1();

	ENABLE_INTERRUPTS(INT_EXT0);
	ENABLE_INTERRUPTS(INT_RDA);
	ENABLE_INTERRUPTS(INT_TIMER4);
	ENABLE_INTERRUPTS(INT_TIMER5);

	while(TRUE){
		output_high(NUC_ON_OFF);

		// Current medition
		I5 = Read_ADC_ports(CH_I5);
		I12 = Read_ADC_ports(CH_I12);
		I24 = Read_ADC_ports(CH_I24);

		// Voltage medition
		m24V = Read_ADC_ports(CH_24V);
		m12V = Read_ADC_ports(CH_12V);
		m05V = Read_ADC_ports(CH_05V);
		mVbat = Read_ADC_ports(CH_VBAT);

		// restar variables
		f_error = 0;
		f_conn = 1;
		f_conSta = 0;
		f_begin = 0;
		RAM_error = 0;
		HDD_error = 0;
		if(flag_info = 1){
			action();
		}
		flag_info = 0;
	}
}
