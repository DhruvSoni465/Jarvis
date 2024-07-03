import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Request failed; check your network connection")
        speak("Sorry, the service is down.")
        return ""

# Function to handle commands
def handle_command(command):
    if 'play' in command:
        song = command.replace('play', '')
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"Current time is {time}")
    elif 'search for' in command:
        topic = command.replace('search for', '')
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    else:
        speak("I'm not sure how to help with that.")

# Main loop
if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = listen()
        if command:
            handle_command(command)
