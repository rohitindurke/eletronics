char state;
const int led_pin = 13;

void setup(){
    Serial.begin(9600);
    pinMode(led_pin,OUTPUT);
    Serial.println("Start scanning");
    Serial.println();
}
void loop(){
    while(Serial.available()>0){
        state = Serial.read();
        if(state == '1'){
            digitalWrite(led_pin,HIGH);
        }
        else{
            digitalWrite(led_pin,LOW);
        }
    }
}