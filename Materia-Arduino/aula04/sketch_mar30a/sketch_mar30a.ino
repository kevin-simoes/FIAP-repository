#define ldrPin A0
int ldrValor = 0;
#define ledR 7
#define ledY 6
#define ledG 5

void setup() {
  Serial.begin(9600);
  pinMode(ldrPin, INPUT);
  pinMode(ledR, OUTPUT);
  pinMode(ledY, OUTPUT);
  pinMode(ledG, OUTPUT);
  
}

void loop() {
  ldrValor = analogRead(ldrPin);
  Serial.println(ldrValor);
  delay(2000);
 if(ldrValor>300){
  digitalWrite(ledG, LOW);
  digitalWrite(ledY, HIGH);
  digitalWrite(ledR, LOW);

 }else if(ldrValor>600){
  digitalWrite(ledG, HIGH);
  digitalWrite(ledY, LOW);
  digitalWrite(ledR, LOW);

 }else{
  digitalWrite(ledG, LOW);
  digitalWrite(ledY, LOW);
  digitalWrite(ledR, HIGH);

 }
}
