# A fun way to test your knowledge

import tkinter as tk
import random
from tkinter import messagebox

# Define quiz levels
level_questions = {
    1: [
        {
            "question": "What is Tokenization in NLP?",
            "options": ["Breaking text into smaller chunks", "Removing verbs from sentences", "Changing words to root form", "Removing punctuation"],
            "answer": "Breaking text into smaller chunks"
        },
        {
            "question": "Which of these is a tokenizer in NLTK?",
            "options": ["RegexpTokenizer", "SpacyTokenizer", "DeepTokenizer", "WordVectorizer"],
            "answer": "RegexpTokenizer"
        },
        {
            "question": "Tokenization is useful for?",
            "options": ["Generating charts", "Splitting text for processing", "Removing spaces", "Predicting next words"],
            "answer": "Splitting text for processing"
        },
        {
            "question": "Which one is not a type of tokenizer?",
            "options": ["WordPunctTokenizer", "TreeTokenizer", "WhitespaceTokenizer", "RegexpTokenizer"],
            "answer": "TreeTokenizer"
        },
        {
            "question": "What does RegexpTokenizer use?",
            "options": ["POS tags", "Regular expressions", "Lemmas", "WordNet"],
            "answer": "Regular expressions"
        },
        {
            "question": "Which tokenizer is simplest?",
            "options": ["WhitespaceTokenizer", "RegexpTokenizer", "TreebankTokenizer", "SpacyTokenizer"],
            "answer": "WhitespaceTokenizer"
        }
    ],
    2: [
        {
            "question": "What does stemming do?",
            "options": ["Finds names of entities", "Removes stopwords", "Reduces words to their root form", "Creates tokens from text"],
            "answer": "Reduces words to their root form"
        },
        {
            "question": "Which is more accurate: stemming or lemmatization?",
            "options": ["Stemming", "Lemmatization", "Both", "None"],
            "answer": "Lemmatization"
        },
        {
            "question": "What does the Snowball stemmer do?",
            "options": ["Adds snow emojis", "Another language stemmer", "Accurate stemming", "Stemming based on regex"],
            "answer": "Accurate stemming"
        },
        {
            "question": "Does lemmatization require context and POS tags?",
            "options": ["Yes", "No", "Sometimes", "Never"],
            "answer": "Yes"
        },
        {
            "question": "Which is a stemmer in NLTK?",
            "options": ["WordNetLemmatizer", "SnowballStemmer", "SpacyStemmer", "CleanStem"],
            "answer": "SnowballStemmer"
        },
        {
            "question": "Which library offers lemmatization?",
            "options": ["NumPy", "NLTK", "Matplotlib", "Pandas"],
            "answer": "NLTK"
        }
    ],
    3: [
        {
            "question": "Which library is commonly used for removing stopwords?",
            "options": ["Matplotlib", "NLTK", "NumPy", "Pandas"],
            "answer": "NLTK"
        },
        {
            "question": "What are stopwords?",
            "options": ["Rare words", "Words like 'the', 'is', 'in'", "Names of people", "Only punctuation marks"],
            "answer": "Words like 'the', 'is', 'in'"
        },
        {
            "question": "Which word is a stopword?",
            "options": ["Python", "Beautiful", "is", "Running"],
            "answer": "is"
        },
        {
            "question": "Why remove stopwords?",
            "options": ["Improve grammar", "Reduce noise in analysis", "Add more words", "Increase vocabulary"],
            "answer": "Reduce noise in analysis"
        },
        {
            "question": "Can stopwords vary by language?",
            "options": ["Yes", "No", "Never", "Only in English"],
            "answer": "Yes"
        },
        {
            "question": "Which is not a stopword?",
            "options": ["a", "the", "with", "banana"],
            "answer": "banana"
        }
    ],
    4: [
        {
            "question": "Stemming result of 'Caring' is?",
            "options": ["Care", "Cared", "Car", "Cares"],
            "answer": "Care"
        },
        {
            "question": "What is Named Entity Recognition used for?",
            "options": ["Counting words", "Removing punctuation", "Identifying names/places", "Tokenizing text"],
            "answer": "Identifying names/places"
        },
        {
            "question": "Does NER work on stopwords?",
            "options": ["Yes", "No", "Sometimes", "Always"],
            "answer": "No"
        },
        {
            "question": "What does NER detect?",
            "options": ["Syntax", "Entities like dates and people", "Grammar rules", "Tenses"],
            "answer": "Entities like dates and people"
        },
        {
            "question": "Which library supports NER?",
            "options": ["NumPy", "Spacy", "Matplotlib", "Seaborn"],
            "answer": "Spacy"
        },
        {
            "question": "Which one is an entity?",
            "options": ["run", "city", "Python", "New York"],
            "answer": "New York"
        },
        {
            "question": "How many hearts do you start with?",
            "options": ["3", "4", "5", "6"],
            "answer": "5"
        },
        {
            "question": "What happens when hearts reach zero?",
            "options": ["Skip question", "Lose quiz", "Extra life", "Nothing"],
            "answer": "Lose quiz"
        },
        {
            "question": "What is POS tagging?",
            "options": ["Parts of sentence", "Position of sentence", "Point of sentence", "Part-of-Speech"],
            "answer": "Part-of-Speech"
        },
        {
            "question": "Which tag represents verb?",
            "options": ["NN", "VB", "JJ", "RB"],
            "answer": "VB"
        }
    ]
}

# GUI setup
root = tk.Tk()
root.title("NLP Quiz Level Selector")
root.geometry("400x300")

level_var = tk.IntVar()

def start_quiz():
    level = level_var.get()
    if level not in level_questions:
        return
    root.destroy()
    launch_quiz(level_questions[level])

title = tk.Label(root, text="Select Your NLP Quiz Level", font=("Arial", 16))
title.pack(pady=20)

levels = ["Level 1: Tokenization", "Level 2: + Stemming & Lemma", "Level 3: + Stopwords", "Level 4: Final Boss"]
for idx, name in enumerate(levels, start=1):
    tk.Radiobutton(root, text=name, variable=level_var, value=idx, font=("Arial", 12)).pack(anchor="w", padx=40)

tk.Button(root, text="Start Quiz", command=start_quiz, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

# Quiz launcher function
def launch_quiz(questions):
    score = 0
    question_index = 0
    hearts = 5

    quiz = tk.Tk()
    quiz.title("NLP Quiz Master")
    quiz.geometry("600x400")

    question_label = tk.Label(quiz, text="", font=("Arial", 14), wraplength=500, justify="center")
    question_label.pack(pady=20)

    options_var = tk.StringVar()
    option_buttons = []
    for _ in range(4):
        btn = tk.Radiobutton(quiz, text="", variable=options_var, value="", font=("Arial", 12))
        btn.pack(anchor="w", padx=100)
        option_buttons.append(btn)

    feedback_label = tk.Label(quiz, text="", font=("Arial", 12), fg="green")
    feedback_label.pack()

    hearts_label = tk.Label(quiz, text="❤️❤️❤️❤️❤️", font=("Arial", 16), fg="red")
    hearts_label.pack()

    def update_hearts():
        hearts_label.config(text="❤️" * hearts + " " * (5 - hearts))

    def display_question():
        nonlocal question_index
        if question_index < len(questions):
            q = questions[question_index]
            question_label.config(text=f"Q{question_index+1}: {q['question']}")
            options_var.set("")
            for i in range(4):
                option_buttons[i].config(text=q['options'][i], value=q['options'][i])
            update_hearts()
        else:
            show_result()

    def check_answer():
        nonlocal score, question_index, hearts
        selected = options_var.get()
        
        if selected == "":
            messagebox.showwarning("No selection", "Please choose an answer before submitting.")
            return
        correct = questions[question_index]['answer']
        if selected == correct:
            score += 1
            feedback_label.config(text="✅ Correct!", fg="green")
        else:
            hearts -= 1
            feedback_label.config(text=f"❌ Wrong! Correct: {correct}", fg="red")
            update_hearts()
            if hearts == 0:
                show_result()
                return
        feedback_label.after(2000,lambda:feedback_label.config(text=""))
        question_index += 1
        quiz.after(1000, display_question)

    def show_result():
        for widget in quiz.winfo_children():
            widget.destroy()

        emoji = ""
        message = ""
        final_score = int((score / len(questions)) * 100)

        if final_score >= 90:
            emoji = "🧙‍♂️✨"
            message = "Are you a wizard so cool? Oh wow, maybe you should try teaching next time!"
        elif final_score < 40:
            emoji = "😔📚"
            message = "You gave it a try and that matters. Don't stop now—next time you'll ace it!"
        else:
            emoji = "😎👍"
            message = "Great effort! You're on the path to mastering NLP. Keep it up!"

        result_label = tk.Label(quiz, text=f"Your Score: {final_score}%", font=("Arial", 20))
        result_label.pack(pady=20)

        emoji_label = tk.Label(quiz, text=emoji, font=("Arial", 50))
        emoji_label.pack()

        message_label = tk.Label(quiz, text=message, font=("Arial", 14), wraplength=500, justify="center")
        message_label.pack(pady=10)

    submit_btn = tk.Button(quiz, text="Submit", command=check_answer, font=("Arial", 12), bg="#4CAF50", fg="white")
    submit_btn.pack(pady=10)

    random.shuffle(questions)
    display_question()
    quiz.mainloop()

root.mainloop()