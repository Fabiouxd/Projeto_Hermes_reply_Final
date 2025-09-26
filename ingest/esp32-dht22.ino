#include <DHTesp.h>
#include <Wire.h>
#include <MPU6050.h>

const int DHT_PIN = 15;
const int POT_PIN = 34;

DHTesp dht;
MPU6050 mpu;

struct Registro {
  float temperatura;
  float umidade;
  int16_t ax, ay, az;
  int pot;
};

const int maxRegistros = 100;
Registro dados[maxRegistros];
int totalRegistros = 0;

void setup() {
  Serial.begin(115200);
  dht.setup(DHT_PIN, DHTesp::DHT22);
  Wire.begin();
  mpu.initialize();

  if (mpu.testConnection()) {
    Serial.println("MPU6050 conectado!");
  } else {
    Serial.println("Erro ao conectar MPU6050");
  }

  analogReadResolution(10); // 0-1023
}

void loop() {
  if (totalRegistros < maxRegistros) {
    // Captura os dados
    TempAndHumidity dhtData = dht.getTempAndHumidity();
    int16_t ax, ay, az;
    mpu.getAcceleration(&ax, &ay, &az);
    int potValue = analogRead(POT_PIN);

    // Armazena no vetor
    dados[totalRegistros] = {dhtData.temperature, dhtData.humidity, ax, ay, az, potValue};
    totalRegistros++;
  }

  // Imprime todos os registros
  Serial.println("=== HISTÓRICO DE DADOS COLETADOS ===");
  for (int i = 0; i < totalRegistros; i++) {
    Serial.printf("#%02d | 🌡 %.2f °C | 💧 %.1f %% | 📈 Acel: X:%d Y:%d Z:%d | 🎛 Pot: %d\n",
      i + 1,
      dados[i].temperatura,
      dados[i].umidade,
      dados[i].ax,
      dados[i].ay,
      dados[i].az,
      dados[i].pot
    );
  }
  Serial.println("------------------------------------\n");

  delay(5000); // Espera 5 segundos antes de coletar de novo
}