// Two DC motors on a dual H-bridge driver
const int ENA = 5, IN1 = 7, IN2 = 8;
const int ENB = 6, IN3 = 9, IN4 = 10;

void motor(int en, int a, int b, int speed) {
  // speed: -255 (full back) .. 255 (full forward)
  digitalWrite(a, speed >= 0 ? HIGH : LOW);
  digitalWrite(b, speed >= 0 ? LOW : HIGH);
  analogWrite(en, constrain(abs(speed), 0, 255));
}

void drive(int left, int right) {
  motor(ENA, IN1, IN2, left);
  motor(ENB, IN3, IN4, right);
}

void setup() {
  int pins[] = {ENA, IN1, IN2, ENB, IN3, IN4};
  for (int p : pins) pinMode(p, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  Serial.println("forward");  drive(150, 150);
  delay(1500);
  Serial.println("stop");     drive(0, 0);
  delay(1000);
  Serial.println("spin");     drive(150, -150);
  delay(800);
  Serial.println("backward"); drive(-150, -150);
  delay(1500);
  drive(0, 0);
  delay(3000);
}
