#include <16f506.h>

#device adc=8

#FUSES NOWDT                 	//No Watch Dog Timer
#FUSES HS                    	//High speed Osc (> 4mhz for PCM/PCH) (>10mhz for PCD)
#FUSES NOPROTECT               	//Code protected from reads
#FUSES MCLR                  	//Master Clear pin enabled
#FUSES IOSC8                 	//INTOSC speed 8MHz

#use delay(clock=10000000)

#define LED PIN_C3
#define DELAY 5000


void main(){
    //Example blinking LED program
    while(true){
      output_low(LED);
      delay_ms(DELAY);
      output_high(LED);
      delay_ms(DELAY);
    }
}