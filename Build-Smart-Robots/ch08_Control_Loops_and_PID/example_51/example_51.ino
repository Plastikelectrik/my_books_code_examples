// Protocol from the Pi: "V,<left m/s>,<right m/s>\n"
const int ENA = 5, IN1 = 7, IN2 = 8;
const int ENB = 6, IN3 = 9, IN4 = 10;
const int ENC_L = 2, ENC_LB = 4;
const int ENC_R = 3, ENC_RB = 11;
const float M_PER_TICK = 0.000576;
const float KP = 150, KI = 1500;
const unsigned long PERIOD_MS = 20;

volatile long tl = 0, tr = 0;
float spL = 0, spR = 0, iL = 0, iR = 0;
long lastL = 0, lastR = 0;
unsigned long lastLoop = 0, lastCmd = 0;

void isrL() { tl += digitalRead(ENC_LB) ? -1 : 1; }
void isrR() { tr += digitalRead(ENC_RB) ? -1 : 1; }

void motor(int en, int a, int b, float s) {
  int p = constrain((int)s, -255, 255);
  digitalWrite(a, p >= 0 ? HIGH : LOW);
  digitalWrite(b, p >= 0 ? LOW : HIGH);
  analogWrite(en, abs(p));
}

float pi(float sp, float meas, float &integ,
         float dt) {
  float e = sp - meas;
  float ni = integ + e * dt;
  float out = KP * e + KI * ni;
  if (out > -255 && out < 255) integ = ni;
  if (sp == 0) { integ = 0; return 0; }
  return constrain(out, -255, 255);
}

void setup() {
  int pins[] = {ENA, IN1, IN2, ENB, IN3, IN4};
  for (int p : pins) pinMode(p, OUTPUT);
  pinMode(ENC_L, INPUT_PULLUP);
  pinMode(ENC_LB, INPUT_PULLUP);
  pinMode(ENC_R, INPUT_PULLUP);
  pinMode(ENC_RB, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENC_L),
                  isrL, RISING);
  attachInterrupt(digitalPinToInterrupt(ENC_R),
                  isrR, RISING);
  Serial.begin(115200);
}

void readCommand() {
  if (!Serial.available()) return;
  String s = Serial.readStringUntil('\n');
  if (!s.startsWith("V,")) return;
  int c = s.indexOf(',', 2);
  spL = s.substring(2, c).toFloat();
  spR = s.substring(c + 1).toFloat();
  lastCmd = millis();
}

void loop() {
  readCommand();
  if (millis() - lastCmd > 500) spL = spR = 0;
  if (millis() - lastLoop < PERIOD_MS) return;
  float dt = (millis() - lastLoop) / 1000.0;
  lastLoop = millis();
  noInterrupts();
  long l = tl, r = tr;
  interrupts();
  float vL = (l - lastL) * M_PER_TICK / dt;
  float vR = (r - lastR) * M_PER_TICK / dt;
  lastL = l; lastR = r;
  motor(ENA, IN1, IN2, pi(spL, vL, iL, dt));
  motor(ENB, IN3, IN4, pi(spR, vR, iR, dt));
  Serial.print("O,"); Serial.print(l);
  Serial.print(","); Serial.println(r);
}
