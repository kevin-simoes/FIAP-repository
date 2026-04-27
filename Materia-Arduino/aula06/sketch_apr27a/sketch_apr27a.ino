#include<Servo.h>
#define servoPin 10
#define trigger 7
#define echo 8
#define led 12
int dist = 0;
//Criando o objeto myservo do tipo Servo
Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(led, OUTPUT);
}
void loop() {
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist/58;

  if(dist < 20) {
    digitalWrite(led, HIGH);
    myServo.write(90);
  }else{
    digitalWrite(led, LOW);
    myServo.write(0);
  }

}
