#use fast_io(B)
#use fast_io(C)
#use fast_io(D)
#use fast_io(E)
#use fast_io(F)

/********************************************/
// Flags
/********************************************/
int1 f_begin, f_error, f_conn=1;
char f_satar, f_conSta, HDD_error, RAM_error;
char R1,G1,B1,R2,G2,B2,R3,G3,B3,R4,G4,B4;			// Enter color valued in RGB
int cycles = 2;

void setup(){
	set_tris_B(0b00111111);
	set_tris_C(0b00111111);
	set_tris_D(0b11110100);
	set_tris_E(0b11011000);
//	set_tris_F(0b10111111);
}
/********************************************/
// Port definition
/********************************************/
#define CH_I5		0 		// PIN_B0
#define CH_I12		1 		// PIN_B1
#define CH_I24		2 		// PIN_B2
#define CH_24V		3 		// PIN_B3
#define CH_12V		4 		// PIN_B4
#define CH_05V		5 		// PIN_B5
#define CH_VBAT		6 		// PIN_B6
#define EN24		PIN_B7	// PIN 26
#define EN12		PIN_B8	// PIN 27
#define EN_VBAT		PIN_C15	// PIN 31
#define LED1		PIN_D0	// PIN 42
#define FAN_A		PIN_D1	// PIN 37
#define FAN_B		PIN_D3	// PIN 38
#define SPEAKER		PIN_E0	// PIN 15
#define LED_RGB		PIN_E1	// PIN 14
#define EN_ANA		PIN_E2	// PIN 11
#define Cap_bot		PIN_F0	// PIN 05
#define LED2		PIN_F6	// PIN 01
#define NUC_ON_OFF	PIN_E5	// PIN 08
#define NUC_LED		PIN_E4	// PIN 09