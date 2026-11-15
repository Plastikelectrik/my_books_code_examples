// Protocol: "M,<left>,<right>\n" from the Pi
const int ENA = 5, IN1 = 7, IN2 = 8;
const int ENB = 6, IN3 = 9, IN4 = 10;
unsigned long lastCmd = 0;

void motor(int en, int a, int b, int s) {
  digitalWrite(a, s >= 0 ? HIGH : LOW);
  digitalWrite(b, s >= 0 ? LOW : HIGH);
  analogWrite(en, constrain(abs(s), 0, 255));
}

void setup() {
  int pins[] = {ENA, IN1, IN2, ENB, IN3, IN4};
  for (int p : pins) pinMode(p, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    String line = Serial.readStringUntil('\n');
    if (line.startsWith("M,")) {
      int c = line.indexOf(',', 2);
      int left = line.substring(2, c).toInt();
      int right = line.substring(c + 1).toInt();
      motor(ENA, IN1, IN2, left);
      motor(ENB, IN3, IN4, right);
      lastCmd = millis();
    }
  }
  // Safety: stop if no command for 500 ms
  if (millis() - lastCmd > 500) {
    motor(ENA, IN1, IN2, 0);
    motor(ENB, IN3, IN4, 0);
  }
}
