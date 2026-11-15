#include <Servo.h>
Servo pan;

void setup() {
  pan.attach(3);   // signal wire on pin 3
}

void loop() {
  for (int a = 0; a <= 180; a += 5) {
    pan.write(a);
    delay(30);
  }
  for (int a = 180; a >= 0; a -= 5) {
    pan.write(a);
    delay(30);
  }
}
