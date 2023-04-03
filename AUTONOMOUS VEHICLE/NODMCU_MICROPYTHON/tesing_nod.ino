#define IN1_PIN 15
#define IN2_PIN 13
#define IN3_PIN 0
#define IN4_PIN 5
#define led 16

void setup() {
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  pinMode(IN1_PIN,OUTPUT);
  pinMode(IN2_PIN,OUTPUT);
  pinMode(IN3_PIN,OUTPUT);
  pinMode(IN4_PIN,OUTPUT);

  digitalWrite(led, LOW);
  digitalWrite(IN1_PIN, LOW);
  digitalWrite(IN2_PIN, LOW);
  digitalWrite(IN3_PIN, LOW);
  digitalWrite(IN4_PIN, LOW);
  
}
 

void loop() {
  delay(1000);

  digitalWrite(led, HIGH);
  digitalWrite(IN2_PIN, HIGH);
  digitalWrite(IN3_PIN, HIGH);

  delay(2000);
  digitalWrite(led, LOW);
  digitalWrite(IN2_PIN, LOW);
  digitalWrite(IN3_PIN, LOW);
 
   
}