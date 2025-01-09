#include <Servo.h>

// set pin
const int trigPin = 9;
const int echoPin = 10;
const int servoPin = 3;

// Create object servo
Servo myServo;

// Set the distrance for ultrasonic
const int distanceThreshold = 10;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  myServo.attach(servoPin);
  myServo.write(90);

  Serial.begin(9600);
}

void loop() {
  long duration;
  int distance;
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2;

  // Display the distance in serial moniter
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance <= distanceThreshold) {
    myServo.write(180);
  } else {
    myServo.write(90);
  }

  delay(500);
}
