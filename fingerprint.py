import pyttsx3
import speech_recognition as sr
import random
import serial
import time

# Initialize serial communication with Arduino
arduino = serial.Serial(port='COM2  ', baudrate=9600, timeout=1)  # Change port as needed

# Initialize the voice engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# List of questions and their correct answers
questions = {
    "What is the favorite food of the owner?": "pizza",
    "What is the owner's pet's name?": "Tom",
    "What city was the owner born in?": "tokyo"
}

# Function to listen to user's response 
def listen_to_response():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        response = recognizer.recognize_google(audio).lower()
        print(f"You said: {response}")
        return response
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results from the speech recognition service.")
        return None

# Main function for the voice assistant
def voice_assistant():
    speak("Fingerprint matched. Answer the following questions correctly.")
    correct_answer_flag = False  # Track if correct answer was given

    for _ in range(1):  # Allow two trials
        question, correct_answer = random.choice(list(questions.items()))
        speak(question) # Ask the question
        print(question)
        answer = listen_to_response()  # Get user's response

        if answer and answer == correct_answer:
            print("Correct answer! Access granted.")
            speak("Correct answer! Access granted.")
            

            correct_answer_flag = True
            yes = arduino.readline().decode('utf-8').strip()
            print(yes)
            
            arduino.write(b'o')  # Set flag to True for correct answer
            break  # Exit the loop if answered correctly
        else:
            speak("Incorrect answer. Try again.") 
            arduino.write(b'F')

    # Decide whether to open the lock or trigger the alarm
      # Send 'O' to Arduino for opening the lock
     # Send 'F' to Arduino to trigger the alarm

if __name__ == "__main__":
     # Wait for "MATCHED" signal from Arduino
    print("Waiting for fingerprint match...")
    while True:
        if arduino.in_waiting > 0:
            match_signal = arduino.readline().decode('utf-8').strip()
            if match_signal == 'M':
                voice_assistant()  # Trigger the voice assistant when fingerprint is matched
