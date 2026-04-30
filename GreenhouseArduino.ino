#include "DHT.h"

#define DHTPIN 2   // Digital pin connected to the DHT sensor 
#define DHTTYPE DHT11   // DHT 11 
DHT dht(DHTPIN, DHTTYPE);
float h; // Humidity
float t; // In celcius
float hif; // heat index in Fahrenheit 
float hic; // heat index in Celcius
String json;
const char* ssid = "Ardino";
const char* password = "ArdinoPass123";
const char* serverIP = "192.168.206.137"; // your RHEL box IP
const int serverPort = 1987;

void setup() {
  // put your setup code here, to run once:
  Serial.println(F("DHTxx test!")); 
  dht.begin(); 
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
  // Check if any reads failed and exit early (to try again). 
  if (isnan(h) || isnan(t)) { 
    Serial.println(F("Failed to read from DHT sensor!")); 
    return; 
  }
  h = dht.readHumidity(); // Humidity
  t = dht.readTemperature(); // Celcius
  
  hic = dht.computeHeatIndex(t, h, false); // Compute heat index in Celsius (isFahreheit = false)

  json = "{\"temp\":" + String(t) +
         ",\"humidity\":" + String(h) +
         ",\"heat_index\":" + String(hic) + "}";

  if (client.connect(serverIP, serverPort)) {
      client.println("POST /reading HTTP/1.1");
      client.println("Host: " + String(serverIP));
      client.println("Content-Type: application/json");
      client.println("Content-Length: " + String(json.length()));
      client.println();
      client.println(json);
      Serial.println("Posted: " + json);
      client.stop();
  } else {
      Serial.println("Connection to server failed");
  }
delay(60);
}
