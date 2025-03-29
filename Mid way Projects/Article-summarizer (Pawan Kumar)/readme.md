# Article Summarization using spaCy

## Overview

This project demonstrates how to perform text summarization using the spaCy NLP library. The script processes a given text, extracts key sentences based on word frequency, and generates a concise summary.

## Features

- Uses **spaCy** for NLP processing.
- Tokenizes text into sentences and words.
- Computes word frequency, ignoring stopwords and punctuation.
- Scores sentences based on word importance.
- Extracts the most relevant sentences as the summary.

## Installation of spacy library and English language model

pip install spacy

python -m spacy download en_core_web_sm

## Usage

Run the script in a Python environment:

```python
import spacy
from heapq import nlargest

# Load spaCy English NLP model
nlp = spacy.load("en_core_web_sm")

# Define the Summarization Function
def summarize(text, ratio=0.3):
    doc = nlp(text)
    sentences = list(doc.sents)
    
 # Compute Word Frequency
    word_freq = {}
    for word in doc:
        if not word.is_stop and not word.is_punct:
            word_freq[word.text.lower()] = word_freq.get(word.text.lower(), 0) + 1

# Score Sentences(Each sentence is scored based on the sum of word frequencies of words in that sentence)

    sentence_scores = {sent: sum(word_freq.get(word.text.lower(), 0) for word in sent) for sent in sentences}
    num_sentences = max(1, int(len(sentences) * ratio))
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
# Joins the selected sentences into a final summary.
    return " ".join(sent.text for sent in summary_sentences)

# Example Usage
article = """
Success is not an overnight achievement but a journey of dedication, hard work, and continuous learning.
Setting realistic goals and maintaining discipline helps in staying focused.
Developing skills, gaining knowledge, and staying updated with industry trends enhance personal and professional growth.
A positive mindset and self-confidence play a crucial role in pushing forward despite difficulties.
Overcoming self-doubt and believing in one’s abilities create a strong foundation for success.
Seeking mentorship from experienced individuals accelerates learning and avoids common pitfalls.
"""

summary = summarize(article)
print("Summary:\n", summary)
```

## Example Output

```
Summary:
Success is not an overnight achievement but a journey of dedication, hard work, and continuous learning.
Developing skills, gaining knowledge, and staying updated with industry trends enhance personal and professional growth.
A positive mindset and self-confidence play a crucial role in pushing forward despite difficulties.
Overcoming self-doubt and believing in one’s abilities create a strong foundation for success.
Seeking mentorship from experienced individuals accelerates learning and avoids common pitfalls.
```





## Author

**Pawan Kumar**
GitHub: [Kpawankumar][https://github.com/Kpawankumar]

