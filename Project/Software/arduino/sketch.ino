#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *m1 = AFMS.getMotor(1);
Adafruit_DCMotor *m2 = AFMS.getMotor(2);
Adafruit_DCMotor *m3 = AFMS.getMotor(3);
Adafruit_DCMotor *m4 = AFMS.getMotor(4);

void setup() {
    Serial.begin(115200);
    AFMS.begin();
}
 
void loop() {
    if (Serial.available() >= 3) {
        byte axis = Serial.read();
        byte direction = Serial.read();
        byte speed = Serial.read();
        switch (axis) {
          case 0:
            driveY(direction, speed);
            break;
          case 1:
            driveX(direction, speed);
            break;
          case 2:
            rotate(direction, speed);
            break;
        }
    }
}

void setSpeed(byte speed) {
  m1->setSpeed((speed / 6) * 5);
  m2->setSpeed((speed / 6) * 5);
  m3->setSpeed(speed);
  m4->setSpeed((speed / 6) * 5);
}

void driveY(byte direction, byte speed) {

  byte forward = direction == 1 ? FORWARD : BACKWARD;
  byte backward = direction == 1 ? BACKWARD : FORWARD;
  
  m1->run(forward);
  m2->run(forward);
  m3->run(backward);
  m4->run(backward);
  setSpeed(speed);
}

void driveX(byte direction, byte speed) {
  byte forward = direction == 1 ? FORWARD : BACKWARD;
  byte backward = direction == 1 ? BACKWARD : FORWARD;
  
  m1->run(forward);
  m2->run(backward);
  m3->run(backward);
  m4->run(forward);
  setSpeed(speed);
}

void rotate(byte direction, byte speed) {
  byte forward = direction == 1 ? FORWARD : BACKWARD;
  byte backward = direction == 1 ? BACKWARD : FORWARD;
  
  m1->run(backward);
  m2->run(forward);
  m3->run(backward);
  m4->run(forward);
  setSpeed(speed);
}
