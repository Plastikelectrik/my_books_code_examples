#include <Servo.h>

// Pins: adjust to your wiring
// order: hipL, hipR, footL, footR
const int PINS[4] = {2, 3, 4, 5};
// Trim: correct each servo's center (calibrate!)
int trim[4] = {0, 0, 0, 0};
Servo s[4];

float offset[4] = {90, 90, 90, 90};
float amp[4]    = {25, 25, 20, 20};
float phase[4]  = {0, 0, 90, 90};   // degrees
const float PERIOD_MS = 1200;

const int TRIG = 8, ECHO = 9;

float distanceCm() {
  digitalWrite(TRIG, LOW); delayMicroseconds(2);
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  unsigned long us = pulseIn(ECHO, HIGH, 25000UL);
  return us == 0 ? 999 : us * 0.0343 / 2.0;
}

void stand() {
  for (int i = 0; i < 4; i++)
    s[i].write(90 + trim[i]);
}

void setup() {
  for (int i = 0; i < 4; i++) s[i].attach(PINS[i]);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  stand();
  delay(1000);
}

void loop() {
  if (distanceCm() < 15) {         // obstacle: stop
    stand();
    delay(200);
    return;
  }
  float t = millis() / PERIOD_MS;  // cycles
  for (int i = 0; i < 4; i++) {
    float a = 2 * PI * t + radians(phase[i]);
    float deg = offset[i] + amp[i] * sin(a);
    s[i].write((int)deg + trim[i]);
  }
  delay(15);                       // about 60 Hz
}
