#include <Servo.h>
#include <string.h>
#include <SoftwareSerial.h>
#include <TFMPlus.h> 

TFMPlus tfmP; 
SoftwareSerial Serialmoon( 2, 3);
long dezimalnummer = 0;
const int stepPin = 5;
double comp ;
const String comingtext = "sa";
int degree = 0;
int height = 0;
Servo servo1;
int Ergebnis_Sharp [3];
int Ergebnis_Moon [3];
int Flux_Modifikator [3];
int16_t Abstand_Moon = 0;
int16_t Flux_Moon = 0;
int16_t Temperatur_Moon = 0;
long int mil1 = 0;
long int mil2 = 0;

void setup() {
  pinMode(8, OUTPUT);
  pinMode(A0, INPUT);
  servo1.attach(7);
  servo1.write(height);
  pinMode(stepPin, OUTPUT);
  Serial.begin( 9600);
  Serialmoon.begin( 115200);  
  delay(100);              
  
    tfmP.begin( &Serialmoon);
    tfmP.sendCommand( SOFT_RESET, 0);
    if( tfmP.sendCommand( GET_FIRMWARE_VERSION, 0))
    {
        printf( "%1u.", tfmP.version[ 0]);
        printf( "%1u.", tfmP.version[ 1]);
        printf( "%1u\r\n", tfmP.version[ 2]);
    }
    if( tfmP.sendCommand( SET_FRAME_RATE, FRAME_10))
    {
        printf( "%2uHz.\r\n", FRAME_20);
    }
}

void turn() {
  for (int z = 0; z < 11; z++) {
        digitalWrite(stepPin, HIGH);
        delayMicroseconds(312.5);
        digitalWrite(stepPin, LOW);
        delayMicroseconds(312.5);
      }
     dezimalnummer = dezimalnummer + 0,111111111;
    //delay(20);
  if (dezimalnummer > 1) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(312.5);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(312.5);
    dezimalnummer = dezimalnummer - 1;
    }
  }
  
void upper() {
    degree = 0;
    servo1.write(height);
    height = height + 10;
    delay(500);
  }
void bekle() {
  while(1) {
    if (Serial.available() > 0) {
      return;
      }
     }
  }

void loop() {
  bekle();
  Serial.println(comingtext);
  for (int o = 0; o < 8; o++) {
    for (int y = 0; y < 72; y++) {
      int Sharpabstand = 0;
      int Sharptotalabstand = 0;
      int Moonabstand = 0;
      unsigned long Gewichtfurabstand = 0;
      long Totalflux = 0;
      int Anzahl_Wiederholungen_Moon = 0;
      int Anzahl_Wiederholungen_Sharp = 0;
      for(int i = 0; i < 3; i++) {
        comp = 9604.8 / analogRead(A0);
        Sharpabstand = pow( comp, 1.0649627263);
        tfmP.getData( Abstand_Moon, Flux_Moon, Temperatur_Moon);
        if(Flux_Moon > 1300) {
          Serial.print("Single:");
          Serial.println(Abstand_Moon);
          Ergebnis_Moon[Anzahl_Wiederholungen_Moon] = Abstand_Moon;
          Flux_Modifikator[Anzahl_Wiederholungen_Moon] = Flux_Moon;
          Totalflux += Flux_Moon;
          Anzahl_Wiederholungen_Moon += 1;
          }
        if(20 > Sharpabstand > 125) {
            //Serial.println(Sharpabstand);
            Ergebnis_Sharp[Anzahl_Wiederholungen_Sharp] = Sharpabstand;
            Anzahl_Wiederholungen_Sharp += 1;
            Sharptotalabstand += Sharpabstand;
        }
        delay(100);
      }
      //Serial.println(Totalflux);
      for(int i = 0; i < Anzahl_Wiederholungen_Moon; i++) {
      long GFA = long(Ergebnis_Moon[i]) * long(Flux_Modifikator[i]);
      //Serial.println(GFA);
      Gewichtfurabstand += GFA;

      //Moonabstand += (Ergebnis_Moon[i] * (Flux_Modifikator[i] / Totalflux));
      //Serial.print("MOON:"); Serial.println(Ergebnis_Moon[i]); Serial.println(Flux_Modifikator[i]);
      //Serial.println(Gewichtfurabstand);
      }
      //Serial.print(Totalflux);
      Moonabstand = round(Gewichtfurabstand / float(Totalflux));
      Sharptotalabstand /= float(Anzahl_Wiederholungen_Sharp);
      Serial.print(height);
      Serial.print(degree);
      Serial.print(" ");
      Serial.println(Moonabstand);
      Serial.print(int(90 - height));
      int grad_2 = 180 + degree;
      if (grad_2 > 359) {
        Serial.print(int(grad_2 - 360));
      }
      else {
        Serial.print(grad_2);
      }
      Serial.print(" ");
      Serial.println(Sharptotalabstand);
      //mil2 = millis();
      if( Temperatur_Moon > 55)
      {
        digitalWrite(8, LOW);
        Serial.println("durduk ab");
        delay(100000);
      }
        degree = degree + 5;
        turn();
        delay(60);
      }
  upper();
  }  
  servo1.write(0);
  delay(4000);
  exit(0);
}