import nltk
from nltk.corpus import wordnet
import re

"""
About it!!!



smart helper helps you find meaning, antonymn or synonymn of any word. 
"""
# Download if missing
for resource in ['wordnet', 'omw-1.4']:
    try:
        nltk.data.find(f'corpora/{resource}')
    except LookupError:
        nltk.download(resource)

# Synonyms
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# Antonyms
def get_antonyms(word):
    antonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            for ant in lemma.antonyms():
                antonyms.add(ant.name())
    return list(antonyms)

# Meaning
def get_meaning(word):
    syns = wordnet.synsets(word)
    return syns[0].definition() if syns else None

# Smart helper
def smartHelper(sentence):
    sentence = sentence.lower()

    # Patterns to detect
    meaning_patterns = [
        r"what does (\w+) mean", r"define (\w+)", r"meaning of (\w+)"
    ]
    synonym_patterns = [
        r"synonym[s]* of (\w+)", r"other words for (\w+)", r"similar to (\w+)"
    ]
    antonym_patterns = [
        r"antonym[s]* of (\w+)", r"opposite of (\w+)",r"opposite word for (\w+)"
    ]

    # Check intent and extract word
    for pattern in meaning_patterns:
        match = re.search(pattern, sentence)
        if match:
            word = match.group(1)
            meaning = get_meaning(word)
            print(f"📘 Meaning of '{word}': {meaning if meaning else 'Not found'}")
            return

    for pattern in synonym_patterns:
        match = re.search(pattern, sentence)
        if match:
            word = match.group(1)
            syns = get_synonyms(word)
            print(f"🔁 Synonyms of '{word}': {syns[:5] if syns else 'Not found'}")
            return

    for pattern in antonym_patterns:
        match = re.search(pattern, sentence)
        if match:
            word = match.group(1)
            ants = get_antonyms(word)
            print(f"↔️ Antonyms of '{word}': {ants[:5] if ants else 'Not found'}")
            return

    print("❓ Sorry, I didn’t understand. Try asking for meaning, synonym, or antonym.")

while True:
    user_input = input("Enter your sentence: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye! See you next time.")
        break
    smartHelper(user_input)