#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>

// Fingerprint sensor and Serial communication setup
SoftwareSerial mySerial(2, 3); // RX, TX for R307
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

const int relayPin = 8; // Relay for electric lock
const int buzzerPin = 9; // Buzzer pin
int failedAttempts = 0;

void setup() {
  Serial.begin(9600);
  finger.begin(57600);
  
  pinMode(relayPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  digitalWrite(relayPin, LOW); // Lock closed initially
  digitalWrite(buzzerPin, LOW); // Buzzer off initially

  if (finger.verifyPassword()) {
    Serial.println("Fingerprint sensor found!");
  } else {
    Serial.println("Fingerprint sensor not detected!");
    while (1);
  }

  Serial.println("Waiting for valid fingerprint...");
}

void loop() {
  int result = finger.getImage();
  
  if (result == FINGERPRINT_OK) {
    result = finger.image2Tz();
    if (result == FINGERPRINT_OK) {
      result = finger.fingerFastSearch();
      if (result == FINGERPRINT_OK) {
        Serial.println("Fingerprint matched.");
        Serial.write('M');  // Send 'M' to Python to indicate a match
        failedAttempts = 0; // Reset failed attempts
        delay(1000);
     

        // Wait for Python to verify and respond with 'O' for unlock or 'F' for failed
        while (Serial.available() == 0) {}
      //  char response = '\0';

        // if (strlen(response) > 1){
        //   ;
        // }
        char response = Serial.read();
        
        if (response == 'o') { // Correct answer
          unlockDoor();
        } else if (response == 'F') { // Incorrect answer
          failedAttempts++;
          if (failedAttempts >= 1) { // After 3 failed attempts
            triggerAlarm();
          }
        }
      } else {
        Serial.println("No match found.");
        failedAttempts++;
        delay(2000);
      }
    }
  }
}


  void unlockDoor() {
  Serial.write("Unlocking the door...");
  digitalWrite(relayPin, HIGH); // Relay on to unlock the door
  delay(5000); // Keep the lock open for 5 seconds
  digitalWrite(relayPin, LOW); // Lock the door again
  Serial.println("Door unlocked");  // Print when the door is unlocked
}



// Function to trigger alarm (buzzer)
void triggerAlarm() {
  Serial.println("Triggering alarm...");
  for (int i = 0; i < 5; i++) {
    digitalWrite(buzzerPin, HIGH);
    delay(500);
    digitalWrite(buzzerPin, LOW);
    delay(500);
  }
  failedAttempts = 0; // Reset after alarm
}