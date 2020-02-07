int time_off = 0;

#ifndef NUC_interface

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

#define NUC_interface

#endif