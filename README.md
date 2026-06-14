# Voice-Enabled Virtual Assistant Using Machine Learning

## Project Overview

The Voice-Enabled Virtual Assistant is a Machine Learning-based desktop application that listens to user voice commands, predicts the intended action using Natural Language Processing (NLP), and performs tasks automatically.

The system uses Speech Recognition for voice input, Machine Learning for intent classification, and Text-to-Speech for voice responses.

---

## Developed By

**R. Shrinidhi**

Department of Computer Science / Artificial Intelligence & Data Science

---

## Objective

To develop an intelligent voice assistant capable of understanding spoken commands and performing various tasks such as:

* Opening websites
* Opening system applications
* Playing music on YouTube
* Searching information on Google
* Setting reminders
* Providing date and time information
* Responding through voice output

---

## Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Multinomial Naive Bayes
* CountVectorizer

### Speech Processing

* SpeechRecognition
* PyAudio
* pyttsx3

### Automation

* WebBrowser
* OS Module
* PyWhatKit

### Data Handling

* Pandas

---

## System Architecture

Voice Input
↓
Speech Recognition
↓
Text Command
↓
Machine Learning Model
↓
Intent Prediction
↓
Task Execution
↓
Voice Response

---

## Features

### Website Automation

* Open YouTube
* Open Google

### Application Control

* Open Calculator
* Open Notepad

### Information Services

* Tell current time
* Tell current date
* Google search

### Entertainment

* Play songs on YouTube

### Productivity

* Create reminders
* Store reminders in a text file

### Voice Interaction

* Listen to user commands
* Speak responses back to the user

---

## Dataset Intents

The model is trained to recognize the following intents:

| Command Type    | Intent          |
| --------------- | --------------- |
| Open YouTube    | open_youtube    |
| Open Google     | open_google     |
| Tell Time       | tell_time       |
| Play Music      | play_music      |
| Open Calculator | open_calculator |
| Open Notepad    | open_notepad    |
| Set Reminder    | set_reminder    |
| Google Search   | google_search   |
| Tell Date       | tell_date       |
| Exit Assistant  | exit            |

---

## Project Structure

```text
VirtualAssistant/
│
├── dataset.csv
├── model.py
├── main.py
├── model.pkl
├── vectorizer.pkl
├── reminders.txt
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd VirtualAssistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run:

```bash
python model.py
```

This will generate:

* model.pkl
* vectorizer.pkl

---

## Running the Assistant

Run:

```bash
python main.py
```

---

## Example Voice Commands

* Open YouTube
* Open Google
* What is the time
* Tell me today's date
* Open Calculator
* Open Notepad
* Search Python Programming
* Play Believer Song
* Set Reminder
* Exit

---

## Machine Learning Model

### Algorithm Used

Multinomial Naive Bayes

### Text Vectorization

CountVectorizer

### Workflow

1. Convert text commands into numerical vectors.
2. Train the Naive Bayes classifier.
3. Predict the user's intent.
4. Execute the corresponding action.

---

## Future Enhancements

* Weather Forecast Integration
* WhatsApp Message Automation
* Email Sending Feature
* AI Chatbot Integration
* GUI Interface using Tkinter
* Voice Authentication
* Multi-language Support
* Smart Reminder Notifications

---

## Conclusion

The Voice-Enabled Virtual Assistant demonstrates the practical application of Machine Learning, Speech Recognition, and Automation techniques. The project successfully converts voice commands into executable actions and provides an interactive user experience through voice-based communication.

---

## Author

**R. Shrinidhi**

Machine Learning Project

2026
