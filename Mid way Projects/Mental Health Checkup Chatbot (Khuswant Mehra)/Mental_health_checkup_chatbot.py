
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random
import tkinter as tk
from tkinter import Scrollbar, Text, Button, END

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

lemmatizer = WordNetLemmatizer()
model = load_model('Model/healthcheckup_chatbot_model.h5')
intents = json.loads(open('D:\AIPlaneTech\mental_Health_chatbot\mentahealth_faqs_\intents.json').read())
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
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            return random.choice(i['responses'])

def chatbot_response(msg):
    ints = predict_class(msg, model)
    return get_response(ints, intents)

#creating GUI with tkinter
import tkinter as tk
import random

class ChatBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Checkup Chatbot")
        self.root.geometry("720x600")
        self.root.resizable(width=True, height=True)
        self.root.configure(bg="#a9a9a9")

        # Full list of suggestions
        self.suggestions = pickle.load(open('Model\suggestions.pkl', 'rb'))

        # Track if the first message has been sent
        self.first_message_sent = False

        # Show initial suggestions (first 5 elements)
        self.current_suggestions = self.suggestions[:5]

        self.create_widgets()

    def create_widgets(self):
        # Chat window
        self.chat_log = tk.Text(self.root, bd=1, bg="#dcdcdc", height=18, width=90, font=("Arial", 11), wrap='word')
        self.chat_log.config(state='disabled')
        self.chat_log.tag_config("user_tag", foreground="#0055ff", font=("Arial", 13, "bold"))
        self.chat_log.tag_config("bot_tag", foreground="#ff5500", font=("Arial", 13, "bold"))
        self.chat_log.tag_config("chat_text", font=("Arial", 13))

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.root, command=self.chat_log.yview, bg="#a9a9a9")
        self.chat_log['yscrollcommand'] = self.scrollbar.set

        # Suggestions Frame
        self.suggestion_frame = tk.Frame(self.root, bg="#a9a9a9")
        self.suggestion_buttons = []

        # Create first set of suggestions
        self.update_suggestion_buttons()

        # Input Box
        self.entry_box = tk.Text(self.root, bd=0, bg="#dcdcdc", width=70, height=3, font=("Arial", 11), wrap='word')
        self.entry_box.bind("<Return>", self.send)

        # Send Button (Square with Curved Edges)
        self.send_button = tk.Canvas(self.root, width=60, height=60, bg="#a9a9a9", highlightthickness=0)
        self.create_round_rect(self.send_button, 5, 5, 55, 55, radius=10, fill="#6495ED", outline="#000000")
        self.send_text = self.send_button.create_text(30, 30, text="Send", font=("Verdana", 10, 'bold'), fill="white")
        self.send_button.bind("<Button-1>", self.send)

        # Place components
        self.scrollbar.place(x=700, y=6, height=486)
        self.chat_log.place(x=6, y=6, height=486, width=690)
        self.suggestion_frame.place(x=6, y=495, width=690, height=30)  # Place above input box
        self.entry_box.place(x=50, y=530, height=50, width=510)
        self.send_button.place(x=580, y=525)

    def create_round_rect(self, canvas, x1, y1, x2, y2, radius=10, **kwargs):
        """Draws a rounded rectangle on the canvas"""
        points = [
            x1+radius, y1, x2-radius, y1, x2, y1, x2, y1+radius,
            x2, y2-radius, x2, y2, x2-radius, y2, x1+radius, y2,
            x1, y2, x1, y2-radius, x1, y1+radius, x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)

    def update_suggestion_buttons(self):
        """Updates the suggestion buttons"""
        # Clear old buttons
        for widget in self.suggestion_frame.winfo_children():
            widget.destroy()

        # Create new buttons
        for text in self.current_suggestions:
            btn = tk.Button(self.suggestion_frame, text=text, font=("Arial", 10), bg="#6495ED", fg="white",
                            relief=tk.FLAT, padx=5, pady=2, command=lambda t=text: self.insert_suggestion(t))
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            self.suggestion_buttons.append(btn)

    def insert_suggestion(self, text):
        """Insert suggestion text into the entry box"""
        self.entry_box.delete("1.0", tk.END)
        self.entry_box.insert(tk.END, text)

    def update_suggestions(self):
        """Removes first five elements (if first message) and shuffles remaining ones after every message"""
        if not self.first_message_sent:
            # Remove the first five elements permanently after first message
            if len(self.suggestions) > 5:
                del self.suggestions[:5]
            self.first_message_sent = True  # Flag set to True after first response

        # Shuffle the remaining suggestions after every message
        if self.suggestions:
            random.shuffle(self.suggestions)
            self.current_suggestions = self.suggestions[:5]
            self.update_suggestion_buttons()

    def send(self, event=None):
        msg = self.entry_box.get("1.0", 'end-1c').strip()
        self.entry_box.delete("0.0", tk.END)

        if msg:
            self.chat_log.config(state='normal')
            self.chat_log.insert(tk.END, "\nYou: ", "user_tag")
            self.chat_log.insert(tk.END, msg + '\n', "user_text")

            res = chatbot_response(msg)  # Replace with actual chatbot response function
            self.chat_log.insert(tk.END, "Bot: ", "bot_tag")
            self.chat_log.insert(tk.END, res + '\n', "bot_text")

            self.chat_log.config(state='disabled')
            self.chat_log.yview(tk.END)

            # Update suggestions every time a message is sent
            self.update_suggestions()

# Run the chatbot GUI
root = tk.Tk()
app = ChatBotGUI(root)
root.mainloop()
