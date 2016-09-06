#include <SPI.h>
#include <MFRC522.h>
#include <EEPROM.h>
 
#define RST_PIN 9
#define SS_PIN 10
#define ledPin1 7
#define Buzzer 2
#define ledPin2 3

 
MFRC522 mfrc522(SS_PIN, RST_PIN);
 
String lastRfid = "";
String kart1 = "***Kart ID";
String kart2 = "***Kart ID";
 
MFRC522::MIFARE_Key key;
 
void setup()
{
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(Buzzer, OUTPUT);
}
 
void loop()
{
  //yeni kart okununmadıkça devam etme
  if ( ! mfrc522.PICC_IsNewCardPresent())
  {
    return;
  }
  if ( ! mfrc522.PICC_ReadCardSerial())
  {
    return;
  }
  //kartın UID'sini oku, rfid isimli string'e kaydet
  String rfid = "";
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
    rfid += mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ";
    rfid += String(mfrc522.uid.uidByte[i], DEC);
  }
  //string'in boyutunu ayarla ve tamamını büyük harfe çevir
  rfid.trim();
  rfid.toUpperCase();
  
  if (rfid == lastRfid)
    return;
  lastRfid = rfid;
 

  Serial.println(rfid);
  Serial.println();

    
  tone(Buzzer, 1000, 500);

  //tone(piezoPin, 1000, 500);
  //delay(1000);
  /*digitalWrite(Buzzer,HIGH);
  delay(1000);
  digitalWrite(Buzzer,LOW);*/
  //1 nolu kart okunduysa LED'i yak, 2 nolu kart okunduysa LED'i söndür
 if (rfid == kart1)
  {
    digitalWrite(ledPin1, HIGH);
    digitalWrite(ledPin2, LOW);
  }
  if (rfid == kart2)
  {
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, HIGH);
  }
  Serial.println();
  delay(200);
 
}
 

