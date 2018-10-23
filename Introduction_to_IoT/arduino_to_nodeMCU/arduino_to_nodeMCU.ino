#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>

SoftwareSerial ss(D2,D3); // (Rx,Tx)

float p,q;

void setup()
{
  Serial.begin(9600);
  ss.begin(9600);
}

void loop()
{
  while(ss.available()>0)
  {
    p=ss.parseFloat();
    if(ss.read()=='\n')
    {
      Serial.println(p);
    }

    q=ss.parseFloat();
    if(ss.read()=='\n')
    {
      Serial.println(q);
    }
  }
  delay(2000);
}
