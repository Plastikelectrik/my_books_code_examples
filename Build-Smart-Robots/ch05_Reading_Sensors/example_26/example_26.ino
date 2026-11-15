// Encoder A on pin 2 (interrupt), B on pin 4
const int ENC_A = 2, ENC_B = 4;
volatile long ticks = 0;

void onA() {
  // If B is low when A rises, we turn forward
  if (digitalRead(ENC_B) == LOW) ticks++;
  else ticks--;
}

void setup() {
  pinMode(ENC_A, INPUT_PULLUP);
  pinMode(ENC_B, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENC_A),
                  onA, RISING);
  Serial.begin(115200);
}

void loop() {
  noInterrupts();          // copy safely
  long t = ticks;
  interrupts();
  Serial.print("E,");
  Serial.println(t);
  delay(100);
}
