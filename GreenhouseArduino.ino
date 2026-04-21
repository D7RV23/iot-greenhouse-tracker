#include "DHT.h"

#define DHTPIN 2   // Digital pin connected to the DHT sensor 
#define DHTTYPE DHT11   // DHT 11 
DHT dht(DHTPIN, DHTTYPE);
float h; // Humidity
float t; // In celcius
float hif; // heat index in Fahrenheit 
float hic; // heat index in Celcius

void setup() {
  // put your setup code here, to run once:
  Serial.println(F("DHTxx test!")); 
  dht.begin(); 
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
  // Check if any reads failed and exit early (to try again). 
  if (isnan(h) || isnan(t) { 
    Serial.println(F("Failed to read from DHT sensor!")); 
    return; 
  }
  h = dht.readHumidity(); // Humidity
  t = dht.readTemperature(); // Celcius
  
  hif = dht.computeHeatIndex(f, h); // Compute heat index in Fahrenheit (the default) 
  hic = dht.computeHeatIndex(t, h, false); // Compute heat index in Celsius (isFahreheit = false)

 
