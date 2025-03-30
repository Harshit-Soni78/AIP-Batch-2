import nltk
import heapq
import re

nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def summarize_text_nltk(text, num_sentences=3):
    """Summarizes text by selecting the most important sentences using word frequency."""
    
    sentences = sent_tokenize(text)

    clean_text = re.sub(r'\W', ' ', text.lower()) # Remove special characters

    words = word_tokenize(clean_text)

    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    # Calculate word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Score sentences based on word frequency
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_freq[word]
                else:
                    sentence_scores[sent] += word_freq[word]

    # Get top N sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = "\n".join(summary_sentences)

    return summary

