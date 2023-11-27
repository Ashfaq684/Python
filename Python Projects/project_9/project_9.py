# Project name - Robo Speaker

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Ashfaq")
    while True:
        text_input = input("Enter what you want me to speak: ")
        if text_input == "q":
            break
        speak(text_input)