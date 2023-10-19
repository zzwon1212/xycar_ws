// HC-SR04 Ultrasonic Sensor Arduino Firmware

int trig[4]={2, 4, 6, 8}
int echo[4]={3, 5, 7, 9}

void setup()
{
  Serial.begin(9600); // start serial communication at 9600bps speed
  for (i = 0; i < 4; i++) {
    pinMode(trig[i], OUTPUT); // define trigger pin as output
    pinMode(echo[i], INPUT); // define echo pin as input
  }
}

void loop() {
  long dur[4]={0.0,};
  long dist[4]={0.0,};

  for (i = 0; i < 4; i++) {
    digitalWrite(trig[i], LOW); // Trig pin Low
    delayMicroseconds(2); // 2us delay
    digitalWrite(trig[i], HIGH); // Trig pin High
    delayMicroseconds(10); // 10us delay
    digitalWrite(trig[i], LOW); // Trig pin Low

    // pulseIn() returns pulse signal from pin by micro-seconds
    dur[i] = pulseIn(echo[i], HIGH);
    dist[i] = dur[i] * 170 / 1000; // compute 340/2=170 since it is return time
    if (dist[i] >= 2000 || dist[i] < 0) {
      dist[i] = 0;
    }
  }

  // print distance on serial monitor
  Serial.print(dist[0]);
  Serial.print("mm ");
  Serial.print(dist[1]);
  Serial.print("mm ");
  Serial.print(dist[2]);
  Serial.print("mm ");
  Serial.print(dist[3]);
  Serial.print("mm ");

  delay(50);
}
