#include <30f4011.h>
#define OSC_INTERNAL
#use delay (clock = 120000000)
#fuses FRC_PLL16,NOPROTECT,NOWDT,NOPUT,MCLR

#use RS232(BAUD=9600,BITS=8,PARITY=N,XMIT=PIN_C13,RCV=PIN_C14,STREAM=PC))// UART
#use i2c(Master,Fast,sda=PIN_F2,scl=PIN_F3)// I2C

#use fast_io(B)
#use fast_io(C)
#use fast_io(D)
#use fast_io(E)
#use fast_io(F)

/********************************************/
// General Definiton
/********************************************/
#define LED_RGB		pin_E1	// pin 14
#define LED1		pin_D0	// pin 42
#define LED2		pin_F6	//  
#define SPEAKER		PIN_E0	// pin 15
#define CH_I5		0 		// PIN_B0
#define CH_I12		1 		// PIN_B1
#define CH_I24		2 		// PIN_B2
#define CH_AN3		3 		// PIN_B3
#define CH_AN4		4 		// PIN_B4
#define CH_AN5		5 		// PIN_B5
#define CH_VBAT		6 		// PIN_B6
#define Cap_bot		PIN_F0
#define NUC_ON_OFF	PIN_E5	// PIN 8
#define NUC_LED		PIN_E4	// PIN 9

/********************************************/
// Import Libraies
/********************************************/
// #include <Include\ws2812b.c>
#include <Include\TONOS.c>
#include <Include\NOTAS.c>

/********************************************/
// Global Variables
/********************************************/
int16 I5, I12, I24, AN3, AN4, AN5, VBAT;
int1 aux_binary = true;
char valor = 0; //Captura el dato recibido del dsPIC
int ban = 0;	//Bandera que indica que llego un dato

/********************************************/
// General configuration 
/********************************************/
void setup(){
	set_tris_B(0b00111111);
	set_tris_E(0b11011100);
	set_tris_F(0b10111111);
	set_tris_D(0b11111110);
}

void ADC_setup(){
	SETUP_ADC(ADC_CLOCK_INTERNAL);
	SETUP_ADC_PORTS(sAN0|sAN1|sAN2|sAN3|sAN4|sAN5|sAN6);
}

void INT_setup(){
	ENABLE_INTERRUPTS(INTR_GLOBAL);
	EXT_INT_EDGE(L_TO_H);
	CLEAR_INTERRUPT(INT_EXT0);
}
/********************************************/
// General Functions
/********************************************/
void linea1(){
generate_tone(NOTA_MI[1],negra);
generate_tone(NOTA_MI[1],negra);
generate_tone(NOTA_MI[1],negra);
generate_tone(NOTA_DO[1],negra);
generate_tone(NOTA_MI[1],negra);
generate_tone(NOTA_SOL[1],negra);
generate_tone(NOTA_SOL[0],negra);
}

void linea2(){
  //Segunda línea
generate_tone(NOTA_MI[2],negra);
//generate_tone(NOTA_RE[2],negra);
//generate_tone(NOTA_MI[2],negra);
//generate_tone(NOTA_FA[2],negra);
//generate_tone(NOTA_SOL[2],negra);
//generate_tone(NOTA_LA[2],negra);
//generate_tone(NOTA_SI[2],negra);
//generate_tone(NOTA_DO[2],negra);
}

int16 Read_ADC_ports(int ch){
	SET_ADC_CHANNEL(ch);
	delay_us(10);
	return READ_ADC();
}
// Declaration of time constans 
// Practical estimation of timing waveforms
const int TH0 = 6;//25;//0.9us
const int TH1 = 13;//8;//0.3us
const int TL0 = 14;//8;//0.3us
const int TL1 = 11;//8;//0.3us

// Color  chage  Detection
void RBG(int R,int  B,int G, int pin){
	int i;
	// Green value
	for(i = 0;i<8;i++){
		output_high(LED_RGB);
		if (G&1){
			delay_cycles(TH1-1-4);
			output_low(LED_RGB);
			delay_cycles(TL1-1-9);
		}
		else{
			delay_cycles(TH0-1-5);
			output_low(LED_RGB);
			delay_cycles(TL0-1-6);
		}
		G>>=1;
	}
	// Red value
	for(i = 0;i<8;i++){
		output_high(LED_RGB);
		if (R&1){
			delay_cycles(TH1-1-4);
			output_low(LED_RGB);
			delay_cycles(TL1-1-4);
		}
		else{
			delay_cycles(TH0-1-5);
			output_low(LED_RGB);
			delay_cycles(TL0-1-6);
		}
		R>>=1;
	}
	// Blue value
	for(i = 0;i<8;i++){
		output_high(LED_RGB);
		if (B&1){
			delay_cycles(TH1-1-4);
			output_low(LED_RGB);
			delay_cycles(TL1-1-4);
		}
		else{
			delay_cycles(TH0-1-5);
			output_low(LED_RGB);
			delay_cycles(TL0-1-6);
		}
		B>>=1;
	}
}
/********************************************/
// Interruptions 
/********************************************/
#int_EXT0
void  EXT0_isr(void){
	aux_binary = !aux_binary;
//	OUTPUT_BIT(LED1,aux_binary);
}
#int_RDA
RDA_isr(){
  fgets (valor); //Captura el dato recibido del PIC 1
  ban = 1;		//Indica que llego un dato
  printf ("Recibido %c\n", valor);
}
/********************************************/
// Main Function 
/********************************************/
void main(){
	setup();
	ADC_setup();
	INT_setup();
	enable_interrupts(INT_EXT0);
	enable_interrupts(INT_RDA);
	//Enter color valued in RGB
	int R,G,B;
	int time_off = 0;
	char string[8];
	R = 240;
	G = 240;
	B = 240;
	INPUT(Cap_bot);
	output_high(NUC_ON_OFF);
	int cont=0;
	
	delay_ms(1000);
	
	while(TRUE){
		printf ("Hola %d\n", cont);
//		if (INPUT(Cap_bot)){
//			time_off = 0;
//			while (INPUT(NUC_LED)){						// Turn on NUC
//				output_low(NUC_ON_OFF);
//				delay_ms(55);
//				output_high(NUC_ON_OFF);
//				delay_ms(100);
//			}
//			while(INPUT(Cap_bot) && !INPUT(NUC_LED)){
//				// Main Program
////				output_high(LED1);
////				RBG(R,B,G,LED_RGB);
//				fgets (string);     // warning: unsafe (see fgets instead)
//				delay_ms(50);
//				printf ("It is alredy ON\n");
////				output_low(LED1);
////				I5 = Read_ADC_ports(CH_I5);
//				delay_ms(50);
//			}
//		}
//		else{
//			if (time_off < 5){
//				linea2();
//				time_off++;
//				delay_ms(1000);
//			}
//			while (!INPUT(NUC_LED) && (time_off==5)){	// Turn off NUC
//				time_off++;
//				output_low(NUC_ON_OFF);
//				delay_ms(55);
//				output_high(NUC_ON_OFF);
//				delay_ms(100);
//			}
//			output_high(NUC_ON_OFF);
//		}
		delay_ms(1000);
		cont ++;
	}
}
