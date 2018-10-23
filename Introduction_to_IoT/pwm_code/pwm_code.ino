
int temp = 0;

void setup() {
  
}

void loop() {
  temp = analogRead(A0);

  temp = temp * (255.0/ 1023.0);

  analogWrite(11, temp);
}
