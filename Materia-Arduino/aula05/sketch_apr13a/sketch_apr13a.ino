#include<DHT.h>
#define dhtpin 7
#define dhttype DHT11

int temp = 0;
int umi = 0;

//Tipo do objeto, Nome do objeto
DHT dht(dhtpin, dhttype);

void setup() {
  Serial.begin(9600);
  dht.begin();
  

}

void loop() {

  //Leitura da temperatura
  temp = dht.readTemperature();
  //Leitura da umidade
  umi = dht.readHumidity();

  Serial.println("Temperatura: " + String(temp));
  delay(2000);
  Serial.println("Umidade: " + String(umi));
  delay(2000);


}