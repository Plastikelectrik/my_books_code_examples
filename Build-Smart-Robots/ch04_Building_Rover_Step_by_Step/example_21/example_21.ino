// Rover firmware: motors, encoders, distance, serial
const int ENA = 5, IN1 = 7, IN2 = 8;
const int ENB = 6, IN3 = 9, IN4 = 10;
const int ENC_L = 2, ENC_LB = 4;
const int ENC_R = 3, ENC_RB = 11;
const int TRIG = 12, ECHO = 13;
const float M_PER_TICK = 0.000576;  // calibrate!
const float KP = 150, KI = 1500;
const float STOP_CM = 10.0;

volatile long tl = 0, tr = 0;
float spL = 0, spR = 0, iL = 0, iR = 0;
int rawL = 0, rawR = 0;
bool rawMode = false;
long lastL = 0, lastR = 0;
float distCm = -1;
unsigned long tCtrl = 0, tSonar = 0, tCmd = 0;

void isrL() { tl += digitalRead(ENC_LB) ? -1 : 1; }
void isrR() { tr += digitalRead(ENC_RB) ? -1 : 1; }

void motor(int en, int a, int b, int p) {
  p = constrain(p, -255, 255);
  digitalWrite(a, p >= 0 ? HIGH : LOW);
  digitalWrite(b, p >= 0 ? LOW : HIGH);
  analogWrite(en, abs(p));
}

float piCtl(float sp, float v, float &integ,
            float dt) {
  if (sp == 0) { integ = 0; return 0; }
  float e = sp - v, ni = integ + e * dt;
  float out = KP * e + KI * ni;
  if (out > -255 && out < 255) integ = ni;
  return constrain(out, -255, 255);
}

float sonar() {
  digitalWrite(TRIG, LOW); delayMicroseconds(2);
  digitalWrite(TRIG, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  unsigned long us = pulseIn(ECHO, HIGH, 25000UL);
  return us == 0 ? -1 : us * 0.0343 / 2.0;
}

void parse(String s) {
  int c = s.indexOf(',', 2);
  if (c < 0) return;
  float a = s.substring(2, c).toFloat();
  float b = s.substring(c + 1).toFloat();
  if (s[0] == 'V') { spL = a; spR = b; rawMode = false; }
  if (s[0] == 'M') { rawL = a; rawR = b; rawMode = true; }
  tCmd = millis();
}

void setup() {
  int outs[] = {ENA, IN1, IN2, ENB, IN3, IN4, TRIG};
  for (int p : outs) pinMode(p, OUTPUT);
  int ins[] = {ENC_L, ENC_LB, ENC_R, ENC_RB};
  for (int p : ins) pinMode(p, INPUT_PULLUP);
  pinMode(ECHO, INPUT);
  attachInterrupt(digitalPinToInterrupt(ENC_L),
                  isrL, RISING);
  attachInterrupt(digitalPinToInterrupt(ENC_R),
                  isrR, RISING);
  Serial.begin(115200);
  Serial.setTimeout(5);
}

void loop() {
  if (Serial.available())
    parse(Serial.readStringUntil('\n'));
  unsigned long now = millis();
  if (now - tSonar >= 60) {
    tSonar = now;
    distCm = sonar();
  }
  if (now - tCtrl < 50) return;      // 20 Hz
  float dt = (now - tCtrl) / 1000.0;
  tCtrl = now;
  noInterrupts(); long l = tl, r = tr; interrupts();
  float vL = (l - lastL) * M_PER_TICK / dt;
  float vR = (r - lastR) * M_PER_TICK / dt;
  lastL = l; lastR = r;

  bool timeout = now - tCmd > 500;
  bool forward = rawMode ? (rawL > 0 && rawR > 0)
                         : (spL > 0 && spR > 0);
  bool blocked = forward && distCm > 0 &&
                 distCm < STOP_CM;
  int pl, pr;
  if (timeout || blocked) {
    pl = pr = 0; iL = iR = 0;
  } else if (rawMode) {
    pl = rawL; pr = rawR;
  } else {
    pl = piCtl(spL, vL, iL, dt);
    pr = piCtl(spR, vR, iR, dt);
  }
  motor(ENA, IN1, IN2, pl);
  motor(ENB, IN3, IN4, pr);
  Serial.print("S,"); Serial.print(l);
  Serial.print(","); Serial.print(r);
  Serial.print(","); Serial.println(distCm, 1);
}
