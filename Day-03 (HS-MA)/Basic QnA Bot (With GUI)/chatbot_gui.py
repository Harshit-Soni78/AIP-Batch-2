# Chat Bot UI

import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random
import tkinter as tk
from tkinter import Scrollbar, Text, Button, END

# Ensure necessary NLTK resources are available
def check_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')

check_nltk_resources()

# Load resources
lemmatizer = WordNetLemmatizer()
model = load_model('Model/chatbot_model.h5')
intents = json.loads(open('Data/admission_data.json').read())
words = pickle.load(open('Model/words.pkl', 'rb'))
classes = pickle.load(open('Model/classes.pkl', 'rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"Found in bag: {w}")
    return np.array(bag)

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    
    # Giving a  error....

    # if not ints:
    #     return "I'm sorry, I don't understand. Can you rephrase?"
    
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            return random.choice(i['responses'])

def chatbot_response(msg):
    ints = predict_class(msg, model)
    return get_response(ints, intents)

# Creating GUI with tkinter
class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("College Admission Chatbot")
        self.root.geometry("500x600")
        self.root.resizable(width=False, height=False)
        self.create_widgets()

    def create_widgets(self):
        # Create Chat window
        self.chat_log = Text(self.root, bd=1, bg="white", height="8", width="50", font="Arial", wrap='word')
        self.chat_log.config(state='disabled')

        # Bind scrollbar to Chat window
        self.scrollbar = Scrollbar(self.root, command=self.chat_log.yview, cursor="heart")
        self.chat_log['yscrollcommand'] = self.scrollbar.set

        # Create the box to enter message
        self.entry_box = Text(self.root, bd=0, bg="white", width="29", height="5", font="Arial", wrap='word')
        self.entry_box.bind("<Return>", self.send)

        # Create Button to send message
        self.send_button = Button(self.root, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                                  bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=self.send)

        # Place all components on the screen
        self.scrollbar.place(x=476, y=6, height=486)
        self.chat_log.place(x=6, y=6, height=486, width=470)
        self.entry_box.place(x=6, y=501, height=90, width=360)
        self.send_button.place(x=370, y=501, height=90)

    def send(self, event=None):
        msg = self.entry_box.get("1.0", 'end-1c').strip()
        self.entry_box.delete("0.0", END)

        if msg:
            self.chat_log.config(state='normal')
            self.chat_log.insert(END, "You: " + msg + '\n\n')
            self.chat_log.config(foreground="#442265", font=("Verdana", 12))

            res = chatbot_response(msg)
            self.chat_log.insert(END, "Bot: " + res + '\n\n')

            self.chat_log.config(state='disabled')
            self.chat_log.yview(END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatBotGUI(root)
    root.mainloop()
