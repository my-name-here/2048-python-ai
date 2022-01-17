int analogPin = A0;
int val = 0;

void setup() {
  Serial.begin(19200);
  Serial.flush();
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int val = char(Serial.read()) - '0';
    if (val == 1) {
      Serial.println('r');
    }
    if (val == 0) {
      Serial.println('u');
    }
    if (val == 2) {
      Serial.println('d');
    }
    if (val == 3) {
      Serial.println('l');
    }
  }
}