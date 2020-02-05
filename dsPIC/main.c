#include <30f4011.h>
#device ADC=12
#define OSC_INTERNAL
#use delay (clock = 120000000)
#fuses FRC_PLL16,NOPROTECT,NOWDT,NOPUT,MCLR

#use RS232(BAUD=9600,BITS=8,PARITY=N,XMIT=PIN_C13,RCV=PIN_C14,TIMEOUT=10)// UART
#use i2c(Master,Fast,sda=PIN_F2,scl=PIN_F3)// I2C

/********************************************/
// Import Libraies
/********************************************/
#include <Include\ports.h>
#include <Include\TONOS.c>
#include <Include\NOTAS.c>
#include <Include\serialProtocol.h>

#use fast_io(B)
#use fast_io(C)
#use fast_io(D)
#use fast_io(E)
#use fast_io(F)

/********************************************/
// Global Variables
/********************************************/
int1 aux_binary = true;
int time_off = 0;
char buffer[6];

const float S2I = 1.25*3.0/4095.0;	// Sensor of current
const float S24 = 11.99*3.0/4095.0;	// Sensor of 24 V
const float S12 = 6.19*3.0/4095.0;	// Sensor of 12 V
const float S05 = 2.35*3.0/4095.0;	// Sensor of 05 V

/********************************************/
// General configuration
/********************************************/
void setup(){
	set_tris_C(0b00111111);
	set_tris_B(0b00111111);
	set_tris_E(0b11011000);
	set_tris_F(0b10111111);
	set_tris_D(0b11111110);
}

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
	delay_us(15);
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

void Delay_bip(int n, long frequency, long duration){
	int i;
	// delay with a bip each second
	for (i=0; i<n; i++){
		delay_ms(1000);
		generate_tone(frequency,duration);
	}
}

void sw_NUC(){
	output_low(NUC_ON_OFF);
	delay_ms(55);
	output_high(NUC_ON_OFF);
	delay_ms(100);
}

void shutdown_NUC(){
	int n = 2;
	if (time_off < n){
		time_off++;
		Delay_bip(1,NOTA_MI[2],negra);
	}
	if (time_off==n){
		while (!INPUT(NUC_LED)) sw_NUC();// Turn off NUC
		delay_ms(2500);
		output_low(EN12);				 // Turn off 12V source
		delay_ms(500);
		output_low(EN24);				 // Turn off 12V source
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
//    putc(inp);
    while(inp != '\n'){
        buffer[i] = inp;
        inp = getc();
//        putc(inp);
        i++;
    }
    int n = sizeof(buffer);
    Hex2data(buffer,n);
	ENABLE_INTERRUPTS(int_rda);
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
	
	delay_ms(3000);
	
	int R,G,B;			// Enter color valued in RGB
//	int data_in = 0;
//	int n = 0;
	delay_ms(500);
	output_high(EN12);
	delay_ms(500);
	output_high(EN24);
	delay_ms(500);
	INPUT(Cap_bot);
	
	R = 240;
	G = 240;
	B = 240;
	
	//data2Hex(24.26, 'I');
	//data2Hex(182.26, 'H');
//	buffer = "$1799";
//	int n = sizeof(buffer);
//	Hex2data(buffer,n);
	Delay_bip(1, NOTA_mi[2], corchea);
	generate_tone(NOTA_sol[2],corchea);
	ENABLE_INTERRUPTS(INT_EXT0);
	ENABLE_INTERRUPTS(INT_RDA);
	delay_ms(2000);
	
	while(TRUE){
		int16 I5, I12, I24, m24V, m12V, m05V, VBAT;
		output_high(NUC_ON_OFF);
		enable_interrupts(int_rda);
		
		// Current medition
		I5 = Read_ADC_ports(CH_I5);
		I12 = Read_ADC_ports(CH_I12);
		I24 = Read_ADC_ports(CH_I24);
		// Voltage medition
		output_high(EN_ANA);
		delay_us(20);
		m24V = Read_ADC_ports(CH_24V);
		m12V = Read_ADC_ports(CH_12V);
		m05V = Read_ADC_ports(CH_05V);
		
		if (INPUT(Cap_bot)){
			output_high(FAN_B);
			
			send_serial(data2Hex(I5*S2I, 'I'));
			send_serial(data2Hex(I12*S2I, 'I'));
			send_serial(data2Hex(I24*S2I, 'I'));
			send_serial(data2Hex(m05V*S05, 'V'));
			send_serial(data2Hex(m12V*S12, 'V'));
			send_serial(data2Hex(m24V*S24, 'V'));
			//output_low(EN_ANA);
			//delay_us(20);
			//m05V = Read_ADC_ports(CH_05V);
			//printf ("V05 = %.3f\n", m05V*S05);
			
//			time_off = 0;
//			if (INPUT(NUC_LED)){
//				sw_NUC(); 			// Turn on NUC
//				delay_ms(120000);
//			}else{
//				/********************************************/
//				// Main Program
//				/********************************************/
//				
//				printf ("Hola\t%d\n", cont);
////				output_high(LED1);
////				RBG(R,B,G,LED_RGB);
////				fgets (string);     // warning: unsafe (see fgets instead)
////				delay_ms(50);
////				printf ("It is alredy ON\n");
////				output_low(LED1);
////				I5 = Read_ADC_ports(CH_I5);
//				delay_ms(1000);
//				
//			}
		}else{
		output_low(FAN_B);
//			shutdown_NUC();
		}
		delay_ms(1000);
	}
}