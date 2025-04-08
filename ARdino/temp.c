#include<SimpleDHT.h>

int dht11_pin = 14;

SimpleDHT11 dht11 (dht11_pin);

void setup(){
    Serial.begin(9600);
    delay(500);
    Serial.println("temp and humidity senser");

}

void loop(){
    int temp,hum;
    dht11.read(&temp,&hum,NULL);
    Serial.println((int)temp);
    Serial.println("*C");
    Serial.println((int)hum);
    Serial.println("%H");
    delay(1000);
}