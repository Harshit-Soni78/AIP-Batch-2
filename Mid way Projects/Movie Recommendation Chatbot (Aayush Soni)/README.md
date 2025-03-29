# AIPlaneTech

## 📌 Movie Recommendation Chatbot 🎬

### 🌟 Introduction

This project is a Movie Recommendation Chatbot built using Tkinter (GUI), spaCy (NER), and NLTK (Sentiment Analysis). The chatbot recommends movies based on user input, detects actors or genres using Named Entity Recognition (NER), and analyzes user feedback with VADER Sentiment Analysis.

### 🚀 Features

✅ GUI-based chatbot using Tkinter

✅ Named Entity Recognition (NER) to extract actor names

✅ Genre-based movie recommendations

✅ Random movie selection from predefined genres

✅ Sentiment Analysis on user feedback

✅ Feedback buttons for better user interaction

✅ Exit commands ("exit", "quit", "stop")


### 📂 Movie-Recommendation-Chatbot

│-- 📜 movieTellerGUI.ipynb                  # Main chatbot application

│-- 📜 requirements.txt          # Required dependencies

│-- 📜 README.md                 # Project documentation


### 🔧 Installation & Setup

1️⃣ Install Dependencies
pip install -r requirements.txt
cd Movie-Recommendation-Chatbot

2️⃣ Download NLP Resources

import nltk

import spacy

nltk.download('vader_lexicon')  # For Sentiment Analysis

spacy.cli.download("en_core_web_sm")  # For Named Entity Recognition (NER)

3️⃣  Run the Chatbot
movieTellerGUI.ipynb 


### 📜 How It Works

The chatbot extracts movie genres or actor names from user input.

If a genre is detected, it recommends a random movie from that genre.

If an actor is detected, it suggests a random movie starring that actor.

If no relevant info is found, it asks the user for clarification.

After making a suggestion, the chatbot asks for feedback (Yes/No).

Using Sentiment Analysis (VADER), it determines if the user liked the recommendation.


### 🛠 Technologies Used

Python 🐍

Tkinter (for GUI) 🎨

spaCy (for NER) 🤖

NLTK (VADER Sentiment Analysis) 📊

Random Module (for movie selection) 🎲


### 🔮 Future Improvements

Improve NER accuracy with a larger movie dataset

Allow multiple genre/actor input in a single query

Integrate with an online movie API (e.g., TMDb) for better recommendations

Add voice input and responses


### 🤝 Contributing

Want to improve this chatbot? Feel free to fork the repo and submit a pull request.

Fork the project

Create your feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Open a Pull Request
