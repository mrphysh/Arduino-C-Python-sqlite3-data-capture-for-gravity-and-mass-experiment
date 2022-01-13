

#define led_out_8 8
#define led_out_9 9
#define led_out_10 10
#define led_out_11 11
#define led_out_12 12
#define led_out_13 13

//define sensor_in_1 1
#define sensor_in_2 2
#define sensor_in_3 3

#define sensor_in_4 4
#define sensor_in_5 5
#define sensor_in_6 6
#define sensor_in_7 7


/*  Input is 2-7 and output is 8-13
 *   2--9 rotating pendulum
 *   3 -- 10
 *   4--11
 *   5--12
 *   6--13
 *   7--8   rotating endulum
 *   
 *   so the leftmost leds are the rotating pendulum 
*/


boolean val_2;   boolean oldval_2;    boolean skipval_2;   boolean val_3;   boolean oldval_3;                    
boolean val_4;   boolean oldval_4;    boolean skipval_4;  boolean val_5;       boolean oldval_5;  
boolean val_6;   boolean oldval_6;    boolean val_7;       boolean oldval_7; boolean skipval_7;                            //////rotating pendulum  has an extra boolean variable
////////////////////////////////////                                                                                                   called a skip_val
long int mytime_2 = 0 ;  long int oldtime_2 = 0;  long int diftime_2 = 0;
long int mytime_3 = 0 ;  long int oldtime_3 = 0;  long int diftime_3= 0;
long int mytime_4 = 0 ;  long int oldtime_4 = 0;  long int diftime_4 = 0;
long int mytime_5 = 0 ;  long int oldtime_5 = 0;  long int diftime_5 = 0;
long int mytime_6 = 0 ;  long int oldtime_6 = 0;  long int diftime_6 = 0;
long int mytime_7 = 0 ;  long int oldtime_7 = 0;  long int diftime_7 = 0;

void setup() {
  // put your setup code here, to run once:

  pinMode (led_out_8, OUTPUT);  pinMode (led_out_9, OUTPUT);  pinMode (led_out_10, OUTPUT);
  pinMode (led_out_11, OUTPUT);  pinMode (led_out_12, OUTPUT);  pinMode (led_out_13, OUTPUT);
  pinMode (sensor_in_2, INPUT);  pinMode (sensor_in_3, INPUT);  pinMode (sensor_in_4, INPUT);
  pinMode (sensor_in_5, INPUT);  pinMode (sensor_in_6, INPUT);  pinMode (sensor_in_7, INPUT);

  Serial.begin(9600);
}

void loop() {
   
  ///////////////////////////////////////////
//////////////////////////////////////////////////////////
////      SENSOR IN 2 AND LED OUT 9        ROTATING PENDULUM
///////////////////
 ////////////////////////////////   ONE


  val_2 = (digitalRead (sensor_in_2));
  while ((val_2 == HIGH) && (oldval_2 == LOW) && (skipval_2 == HIGH))  {
   
    oldval_2 = val_2;
    digitalWrite (led_out_9, HIGH);
    break;
  }

  ///////////////////////////////////   TWO

  while ((val_2 == LOW) && (oldval_2 == HIGH) && (skipval_2 == HIGH))  {
    oldval_2 = val_2;
    skipval_2 = not skipval_2;
    mytime_2 = micros();
    
    diftime_2 = mytime_2 - oldtime_2;
    Serial.println (diftime_2);

    break;
  }

  ///////////////////////////////////////////////    THREE

  while ((val_2 == HIGH) && (oldval_2 == LOW) && (skipval_2 == LOW))  {
   
    oldval_2 = val_2;
   
 digitalWrite (led_out_9, LOW);
    break;
  }


  //////////////////////////////////////////////    FOUR


  while ((val_2 == LOW) && (oldval_2 == HIGH) && (skipval_2 == LOW))  {
   
    oldval_2 = val_2;
   
   skipval_2 = not skipval_2;
    break;
  }
  oldtime_2 = mytime_2;

//////////////////////////////////////////////////////////////////
  //////////////////////////////////////////////////
  ////////////////////////////////////////
  /////    SENSOR IN 3 AND LED OUT 10  ////
 oldval_3 = val_3;
  val_3 = (digitalRead (sensor_in_3));
  while ((val_3 == HIGH) && (oldval_3 == LOW))  {
    digitalWrite (led_out_10, HIGH);
    break;
  }
  while ((val_3 == LOW) && (oldval_3 == HIGH))  {
    digitalWrite (led_out_10, LOW);
    mytime_3 = micros();
    diftime_3 = mytime_3 - oldtime_3;

    Serial.println (diftime_3);
    break;
  }


  oldtime_3 = mytime_3;
  
  /////////////////////////////////////////////////////
  /////       SENSOR IN 4 AND  LED OUT 11 ////////////
  /////////////     rotating pendulum/////////////                                           ///////////////
  ////////////////////////////////////////////////
  /*
  
*/
 /// /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
  ////////////////////////////////   ONE


  val_4 = (digitalRead (sensor_in_4));
  while ((val_4 == HIGH) && (oldval_4 == LOW) && (skipval_4 == HIGH))  {
   
    oldval_4 = val_4;
    digitalWrite (led_out_11, HIGH);
    break;
    
  }

  ///////////////////////////////////   TWO

  while ((val_4 == LOW) && (oldval_4 == HIGH) && (skipval_4 == HIGH))  {
    oldval_4 = val_4;
    skipval_4 = not skipval_4;
    mytime_4 = micros();
    
    diftime_4 = mytime_4 - oldtime_4;
    Serial.println (diftime_4);

    break;
  }

  ///////////////////////////////////////////////    THREE

  while ((val_4 == HIGH) && (oldval_4 == LOW) && (skipval_4 == LOW))  {
   
    oldval_4 = val_4;
   
 
 digitalWrite (led_out_11, LOW);
    break;
  }


  //////////////////////////////////////////////    FOUR


  while ((val_4 == LOW) && (oldval_4 == HIGH) && (skipval_4 == LOW))  {
   
    oldval_4 = val_4;
   
   skipval_4 = not skipval_4;
    break;
  }
  oldtime_4 = mytime_4;
/////-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
  
//////////////////////////////////////////////////////////
////      SENSOR IN 5 AND LED OUT 12 
 oldval_5 = val_5;
  val_5 = (digitalRead (sensor_in_5));
  while ((val_5 == HIGH) && (oldval_5 == LOW))  {
    digitalWrite (led_out_12, HIGH);
    break;
  }
  while ((val_5 == LOW) && (oldval_5 == HIGH))  {
    digitalWrite (led_out_12, LOW);
    mytime_5 = micros();
    diftime_5 = mytime_5 - oldtime_5;

    Serial.println (diftime_5 + 20000000);                              //  add 20 million and then Python can separate them based on this
    break;
  }


  oldtime_5 = mytime_5;
  //////////////////////////////////////////

  ////      SENSOR IN 6 AND LED OUT 13  
 oldval_6 = val_6;
  val_6 = (digitalRead (sensor_in_6));
  while ((val_6 == HIGH) && (oldval_6 == LOW))  {
    digitalWrite (led_out_13, HIGH);
    break;
  }
  while ((val_6 == LOW) && (oldval_6 == HIGH))  {
    digitalWrite (led_out_13, LOW);
    mytime_6 = micros();
    diftime_6 = mytime_6 - oldtime_6;

    Serial.println (diftime_6 + 30000000);                              //add 30 millin and then python will not have a problem
    break;
  }


  oldtime_6 = mytime_6;
  /////////////////////////////////////////
  ////////////////////////////////////////
  ////      SENSOR IN 7 AND LED OUT 8            ROTATING PENDULUM
///////////////////////////////////////////////////
/////////////////////////////////////////
   ////////////////////////////////   ONE


  val_7 = (digitalRead (sensor_in_7));
  while ((val_7 == HIGH) && (oldval_7 == LOW) && (skipval_7 == HIGH))  {
   
    oldval_7 = val_7;
    digitalWrite (led_out_8, HIGH);
    break;
  }

  ///////////////////////////////////   TWO

  while ((val_7 == LOW) && (oldval_7 == HIGH) && (skipval_7 == HIGH))  {
    oldval_7 = val_7;
    skipval_7 = not skipval_7;
    mytime_7 = micros();
    
    diftime_7 = mytime_7 - oldtime_7;
    Serial.println (diftime_7);

    break;
  }

  ///////////////////////////////////////////////    THREE

  while ((val_7 == HIGH) && (oldval_7 == LOW) && (skipval_7 == LOW))  {
   
    oldval_7 = val_7;
   
 digitalWrite (led_out_8, LOW);
    break;
  }

  //////////////////////////////////////////////    FOUR


  while ((val_7 == LOW) && (oldval_7 == HIGH) && (skipval_7 == LOW))  {
   
    oldval_7 = val_7;
   
   skipval_7 = not skipval_7;
    break;
  }
  oldtime_7 = mytime_7;

  
  
  ////////////////////////////////////////
}
