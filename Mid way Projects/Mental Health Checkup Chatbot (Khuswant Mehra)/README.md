# Mental Health Checkup Chatbot

## Overview

The **Mental Health Checkup Chatbot** is a machine learning-based chatbot designed to assist users by providing responses to common mental health-related queries. It utilizes natural language processing (NLP) techniques to understand user inputs and provide appropriate responses from a predefined set of intents.

## Features

- Uses NLP for understanding and processing user queries.
- Provides responses based on trained intents.
- Graphical User Interface (GUI) built with Tkinter.
- Suggestion-based interaction for better user engagement.
- Model training functionality to enhance chatbot accuracy.

## Project Structure

```
MentalHealthChatbot/
├── Model/
│   ├── healthcheckup_chatbot_model.h5  # Trained chatbot model
│   ├── words.pkl                       # Tokenized words
│   ├── classes.pkl                     # Classes for intent classification
│   ├── suggestions.pkl                  # Predefined response suggestions
│
├── mentahealth_faqs_
│   ├── intents.json                     # Dataset for chatbot responses
│
├── Mental_health_checkup_chatbot.py     # Chatbot application
├── model_training.py                    # Model training script
└── README.md                             # Documentation
```

## Installation & Setup

### Prerequisites

Ensure you have the following dependencies installed:

```bash
pip install numpy keras tensorflow nltk pickle-mixin
```

### Steps to Run the Chatbot

1. **Train the Model (if not already trained):**

   ```bash
   python model_training.py
   ```

   This will generate the trained model and save necessary files in the `Model/` directory.

2. **Run the Chatbot Application:**
   ```bash
   python Mental_health_checkup_chatbot.py
   ```

## Detailed Explanation

### 1. Model Training (`model_training.py`)

- Loads the `intents.json` file containing predefined questions and responses.
- Tokenizes and lemmatizes words.
- Creates training data, including bag-of-words representations.
- Defines a neural network model using Keras and trains it on the processed dataset.
- Saves the trained model and necessary metadata (`words.pkl`, `classes.pkl`, `suggestions.pkl`).

### 2. Chatbot Application (`Mental_health_checkup_chatbot.py`)

- Loads the trained model and necessary metadata.
- Uses a GUI built with Tkinter for user interaction.
- Processes user input, tokenizes, and lemmatizes words.
- Predicts intent using the trained model and provides relevant responses.
- Includes a suggestion mechanism to assist users in asking relevant questions.

## File Descriptions

- **`intents.json`**: JSON file containing predefined patterns and responses.
- **`words.pkl`**: Serialized tokenized words.
- **`classes.pkl`**: Serialized class labels for intent recognition.
- **`suggestions.pkl`**: Predefined response suggestions.
- **`healthcheckup_chatbot_model.h5`**: Trained deep learning model.

## Future Improvements

- Implementing a more advanced deep learning model for better accuracy.
- Enhancing the dataset to include more intents and responses.
- Deploying the chatbot as a web application.

## License

This project is for educational purposes. Feel free to modify and enhance it as needed!

---

## Credits

- Harshit Soni - https://github.com/Harshit-Soni78 -- For source code for Model Training as well as Model Implementation on GUI

- ChatGPT by openAI

- Kaggle user elvis23 - https://www.kaggle.com/elvis23 -- for dataset Mental Health Conversational Data.
---

**Author:** Khushwant Mehra
**Contact:** kmehra.sengg@gmail.com
**Github:** https://github.com/This-is-khushwant
