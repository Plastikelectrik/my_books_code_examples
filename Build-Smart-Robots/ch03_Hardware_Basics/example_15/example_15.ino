// Blink the built-in LED and print a counter
const int LED = LED_BUILTIN;
unsigned long count = 0;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(500);
  digitalWrite(LED, LOW);
  delay(500);
  count++;
  Serial.print("blink ");
  Serial.println(count);
}
