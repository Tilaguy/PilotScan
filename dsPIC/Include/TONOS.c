////////////////// Driver to generate musical tones /////////////////////
////                                                                 ////
////  generate_tone(frequency, duration)     Generates wave at set   ////
////                                         frequency (Hz) for set  ////
////                                         duration (ms)           ////
////                                                                 ////
/////////////////////////////////////////////////////////////////////////
////        (C) Copyright 1996,2003 Custom Computer Services         ////
//// This source code may only be used by licensed users of the CCS  ////
//// C compiler.  This source code may only be distributed to other  ////
//// licensed users of the CCS C compiler.  No other use,            ////
//// reproduction or distribution is permitted without written       ////
//// permission.  Derivative programs created using this software    ////
//// in object code form are not restricted in any way.              ////
/////////////////////////////////////////////////////////////////////////


#ifndef  MUSIC_NOTES
#define  MUSIC_NOTES

//            NOTE                 FREQUENCY
//                     Octave0  Octave1  Octave2  Octave3
const long NOTA_DO[4]  ={ 2093,     4186,    1047,    2093};
const long NOTA_DOS[4] ={ 2217,     4435,    1109,    2217};
const long NOTA_RE[4]  ={ 2349,     4693,    1175,    2349};
const long NOTA_RES[4] ={ 2489,     4978,    1245,    2489};
const long NOTA_MI[4]  ={ 2637,     5274,    1329,    2637};
const long NOTA_FA[4]  ={ 2793,     5588,    1397,    2794};
const long NOTA_FAS[4] ={ 2959,     5920,    1480,    2960};
const long NOTA_SOL[4]  ={ 3135,     6272,    1568,    3136};
const long NOTA_SOLS[4] ={ 3322,     6645,    1661,    3322};
const long NOTA_LA[4]  ={ 3520,     7040,    1760,    3520};
const long NOTA_LAS[4] ={ 3729,     7459,    1865,    3729};
const long NOTA_SI[4]  ={ 3951,     7902,    1976,    3951};
#endif


void do_delay(int ms_delay, int num_ms, int us_delay, int num_us)  {
 int i;

 for(i=0;i<num_ms;i++)
  delay_ms(250);
 delay_ms(ms_delay);
 for(i=0;i<num_us;i++)
  delay_us(250);
 delay_us(us_delay);
}


void generate_tone(long frequency, long duration)
{
   int32 total_delay_time;                      // in microseconds
   long total_ms_delay_time, total_us_delay_time;
   int num_us_delays, num_ms_delays, ms_delay_time, us_delay_time;
   long num_periods;

   total_delay_time = (1000000/frequency)/2-10; // calculate total delay time (10 for error)

   total_ms_delay_time = total_delay_time/1000; // total delay time of ms
   num_ms_delays = total_ms_delay_time/250;     // number of 250ms delays needed
   ms_delay_time = total_ms_delay_time%250;     // left over ms delay time needed

   total_us_delay_time = total_delay_time%1000; // total delay time of us (ms already acounted for)
   num_us_delays = total_us_delay_time/250;     // number of 250us delays needed
   us_delay_time = total_us_delay_time%250;     // left over us delay time needed

   num_periods = ((int32)duration*1000)/(1000000/frequency);

   while((num_periods--) != 0)
   {
      do_delay(ms_delay_time, num_ms_delays, us_delay_time, num_us_delays);
      output_high(SPEAKER);
      do_delay(ms_delay_time, num_ms_delays, us_delay_time, num_us_delays);
      output_low(SPEAKER);
   }

   return;
}
