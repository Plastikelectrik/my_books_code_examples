const int TRIG = 11, ECHO = 12;

float readDistanceCm() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  // wait max 25 ms (about 4 m round trip)
  unsigned long us = pulseIn(ECHO, HIGH, 25000UL);
  if (us == 0) return -1.0;   // no echo
  return us * 0.0343 / 2.0;
}

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Serial.begin(115200);
}

void loop() {
  float d = readDistanceCm();
  Serial.print("D,");
  Serial.println(d, 1);
  delay(60);   // let old echoes fade away
}
