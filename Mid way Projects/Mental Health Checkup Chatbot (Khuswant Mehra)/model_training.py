
import nltk
import json
import pickle
import random
import numpy as np
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import os

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

# Load and process the data
data_file =open('D:\AIPlaneTech\mental_Health_chatbot\mentahealth_faqs_\intents.json').read()
intents = json.loads(data_file)

words = []
classes = []
suggestions = []
documents = []
ignore_words = ['?', '!']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word in the sentence
        if intent.get("tag", "").startswith("fact") or intent.get("tag", "").startswith("greeting"):
            suggestions.append(pattern)
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # Add to documents
        documents.append((w, intent['tag']))
        # Add to classes if not already present
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and lower each word and remove duplicates
words = sorted(list(set([lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words])))

# Sort classes
classes = sorted(list(set(classes)))

# Print data information
print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

# Save words and classes to disk
pickle.dump(words, open('Model\words.pkl', 'wb'))
pickle.dump(classes, open('Model\classes.pkl', 'wb'))
pickle.dump(suggestions, open('Model\suggestions.pkl', 'wb'))

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    # Initialize bag of words
    bag = []
    pattern_words = doc[0]
    # Lemmatize each word
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # Create bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # Create output array
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Shuffle the data and convert to numpy arrays
random.shuffle(training)
training = np.array(training, dtype=object)

# Create train and test lists
train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

print("Training data created")

# Create model
model = Sequential()
model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit and save the model
hist = model.fit(train_x, train_y, epochs=250, batch_size=5, verbose=1)
model.save('Model\healthcheckup_chatbot_model.h5', hist)

print("model created")
