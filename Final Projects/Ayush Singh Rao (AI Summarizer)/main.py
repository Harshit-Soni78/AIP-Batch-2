from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import heapq
import os
import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__)

def get_text_from_url(url):
    """Fetches and extracts text from a given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    article_text = " ".join([para.get_text() for para in paragraphs])
    return article_text

def get_youtube_transcript(video_url):
    """Fetches the transcript of a YouTube video."""
    try:
        video_id = video_url.split("v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return None

def summarize_text(text, num_sentences=3):
    """Summarizes the given text using word frequency."""
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    word_frequencies = {}

    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    max_freq = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return " ".join(summary_sentences)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.form.get("url")
    if data:
        if "youtube.com" in data or "youtu.be" in data:
            article_text = get_youtube_transcript(data)
        else:
            article_text = get_text_from_url(data)
        
        if article_text:
            summary = summarize_text(article_text, num_sentences=5)
            return jsonify({"summary": summary})
    return jsonify({"error": "Invalid URL or no text found."})

if __name__ == '__main__':
    app.run(debug=True)