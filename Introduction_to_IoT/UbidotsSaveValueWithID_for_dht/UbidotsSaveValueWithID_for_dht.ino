
#include <SimpleDHT.h>

#include "UbidotsMicroESP8266.h"

#define TOKEN  "A1E-fweiYloqEDh0e3T1BBjJkD8HW37UDt"  // Put here your Ubidots TOKEN
#define TEMPERATURE "5b8ced96c03f9747e4635e8a" // Put your variable ID here
#define HUMIDITY "5b8cee16c03f974866ef070f" // Put your variable ID here
#define WIFISSID "AndroidAP" // Put here your Wi-Fi SSID
#define PASSWORD "hvnx4566" // Put here your Wi-Fi password
int pinDHT11 = D4;
int T, H;
Ubidots client(TOKEN);
SimpleDHT11 dht11;

void setup(){
     pinMode(pinDHT11, INPUT);
    Serial.begin(115200);
    client.wifiConnection(WIFISSID, PASSWORD);
    //client.setDebug(true); // Uncomment this line to set DEBUG on
}

void loop(){
    Serial.println("======================================");
    Serial.println("Sample DHT................");

    byte temperature = 0;
    byte humidity = 0;
    int err = SimpleDHTErrSuccess;
    if((err = dht11.read(pinDHT11, &temperature,&humidity, NULL))!= SimpleDHTErrSuccess){
      Serial.print("Read DHT11 failed err = ");
      Serial.println(err);
      delay(1000);
      return;
    }
    Serial.print("Sample OK: ");
    Serial.print((int)temperature); Serial.print("*C");
    Serial.print((int)humidity); Serial.print("%");
    client.add(TEMPERATURE, temperature);
    client.add(HUMIDITY, humidity);
    delay(4500);
}
