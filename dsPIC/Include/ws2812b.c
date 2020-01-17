// Declaration of time constans 
// Practical estimation of timing waveforms
const int TH0 = 1;//25;//0.9us
const int TH1 = 1;//8;//0.3us
const int TL0 = 1;//8;//0.3us
const int TL1 = 1;//8;//0.3us

// ON cycle - Send a bit of value one
void one(int pin){     // LED status change to turn OFF      
	output_high(pin);
	delay_cycles(TH1);
	output_low(pin);
	delay_cycles(TL1); 
}
// OFF cycle -  Send a bit of value zero
void zero(int pin){    // LED status change to turn OFF 
	output_high(pin);
	delay_cycles(TH0);
	output_low(pin);
	delay_cycles(TL0);
}


// Color  chage  Detection
void RBG(int R,int  B,int G, int pin){
	int i;
	// Green value
	for(i = 0;i<8;i++){
		(G&1) ? one(pin) : zero(pin);
//		if (G&1)
//			one(pin);
//		else
//			zero(pin);
		G = G>>1;
	}
	// Red value
	for(i = 0;i<8;i++){
		(R&1) ? one(pin) : zero(pin);
//		if (R&1)
//			one(pin);
//		else
//			zero(pin);
		R = R>>1;
	}
	// Blue value
	for(i = 0;i<8;i++){
		(B&1) ? one(pin) : zero(pin);
//		if (B&1)
//			one(pin);
//		else
//			zero(pin);
		B = B>>1;
	}
}