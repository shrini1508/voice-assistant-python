import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pandas as pd
import os
import pywhatkit

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------- ML TRAINING ----------------

data = pd.read_csv("dataset.csv")

X = data["command"]
y = data["intent"]

vectorizer = CountVectorizer()

X_vectors = vectorizer.fit_transform(X)

model = MultinomialNB()

model.fit(X_vectors, y)

# ---------------- VOICE ----------------

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        return ""

# ---------------- PREDICTION ----------------

def predict_intent(command):

    command_vector = vectorizer.transform([command])

    prediction = model.predict(command_vector)

    return prediction[0]

# ---------------- ACTION ----------------

def execute_intent(intent,command):

    if intent == "open_youtube":
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif intent == "open_google":
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif intent == "tell_time":
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
    
    elif intent == "open_calculator":
        speak("Opening calculator")
        os.system("calc")

    elif intent == "open_notepad":
        speak("Opening notepad")
        os.system("notepad")

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif intent == "set_reminder":
        speak("What should I remind you?")
        reminder = listen()
        with open("reminders.txt", "a") as file:
            file.write(reminder + "\n")
        speak("Reminder saved")

    elif intent == "google_search":
        search = command.replace("search", "")
        speak("Searching Google")
        webbrowser.open(f"https://www.google.com/search?q={search}")

    elif intent == "tell_date":
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
            
    else:
        speak("I don't understand")

# ---------------- MAIN ----------------

speak("Hello, I am your assistant")

command = listen()

intent = predict_intent(command)

print("Predicted Intent:", intent)

execute_intent(intent,command)