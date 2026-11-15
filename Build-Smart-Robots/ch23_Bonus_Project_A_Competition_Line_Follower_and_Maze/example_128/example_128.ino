const int N = 5;
const int PINS[N] = {A0, A1, A2, A3, A4};
int lo[N], hi[N];

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < N; i++) {
    lo[i] = 1023;
    hi[i] = 0;
  }
  unsigned long t0 = millis();
  while (millis() - t0 < 3000) {  // sweep over line
    for (int i = 0; i < N; i++) {
      int v = analogRead(PINS[i]);
      lo[i] = min(lo[i], v);
      hi[i] = max(hi[i], v);
    }
  }
}

long position(bool &found) {
  long num = 0, den = 0;
  for (int i = 0; i < N; i++) {
    int v = analogRead(PINS[i]);
    long n = 0;
    if (hi[i] > lo[i])
      n = (long)(v - lo[i]) * 1000 / (hi[i] - lo[i]);
    n = constrain(n, 0, 1000);
    num += n * (i * 1000 - 2000);   // -2000..2000
    den += n;
  }
  found = den > 300;
  return found ? num / den : 0;
}

void loop() {
  bool found;
  long p = position(found);
  Serial.println(found ? p : 9999);  // 9999 = lost
  delay(20);
}
