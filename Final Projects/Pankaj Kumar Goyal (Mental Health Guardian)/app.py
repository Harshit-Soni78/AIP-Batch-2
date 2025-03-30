from flask import Flask, request, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
import tweepy
import os
from dotenv import load_dotenv
import time

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session management

# Distress threshold
DISTRESS_THRESHOLD = 1  # Set your threshold here

# Load environment variables
load_dotenv()


# Bearer Token for X API v2
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")


# Setup Tweepy Client for v2 API (for fetching tweets)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to check and download NLTK resources
def ensure_nltk_resource(resource, name):
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(name)

# Pre-saved user IDs to save requests
USER_IDS = {"elonmusk": "44196397", "nasa": "11348282"}  # Add more as needed

def get_user_id(username):
    if username in USER_IDS:
        return USER_IDS[username]
    try:
        user = client.get_user(username=username)
        if not user.data:
            return None  # Handle case where user doesn't exist
        USER_IDS[username] = user.data.id  # Cache it
        return user.data.id
    except tweepy.TweepyException as e:
        print(f"Twitter API error for {username}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting user ID for {username}: {e}")
        return None

def fetch_user_tweets(username, max_tweets=10):
    user_id = get_user_id(username)
    if not user_id:
        return []  # Return empty list if user_id couldn't be fetched
    try:
        response = client.get_users_tweets(id=user_id, max_results=max_tweets,
                                          tweet_fields=["created_at"])
        if not response.data:
            return []  # Return empty list if no tweets found
        tweets = [{"text": tweet.text, "id": tweet.id, "created_at": tweet.created_at} for tweet in response.data]
        return tweets[:max_tweets]
    except tweepy.TweepyException as e:
        print(f"Twitter API error fetching tweets for {username}: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error fetching tweets for {username}: {e}")
        return []

# Check and download required NLTK dependencies
ensure_nltk_resource('tokenizers/punkt', 'punkt')
ensure_nltk_resource('corpora/stopwords', 'stopwords')
ensure_nltk_resource('corpora/wordnet', 'wordnet')
ensure_nltk_resource('sentiment/vader_lexicon', 'vader_lexicon')


# Initialize tools with error handling
try:
    nlp = spacy.load('en_core_web_md')
except OSError:
    print("Error: 'en_core_web_md' not found. Run 'python -m spacy download en_core_web_md'.")
    exit(1)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sia = SentimentIntensityAnalyzer()

# Load concern keywords from file
file_path = "concern_keywords.txt"  # Ensure file exists in same directory
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    concern_keywords = [line.strip() for line in lines] 



# Analyze a post
def analyze_post(post, threshold=0.05):
    tokens = word_tokenize(post["text"].lower())
    cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens
                      if token.isalnum() and token not in stop_words]
    flagged_keywords = [kw for kw in cleaned_tokens if kw in concern_keywords]
    doc = nlp(post["text"])
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentiment = sia.polarity_scores(post["text"])
    sentiment_label = "Positive" if sentiment['compound'] > threshold else \
                      "Negative" if sentiment['compound'] < -threshold else "Neutral"
    alert = "Potential distress detected" if (sentiment['compound'] < -threshold and flagged_keywords) else "None"
    return {
        "keywords": cleaned_tokens,
        "flagged_keywords": flagged_keywords,
        "entities": entities,
        "sentiment": sentiment_label,
        "compound_score": sentiment['compound'],
        "alert": alert,
        "text": post["text"],
        "id": post["id"],
        "created_at": post["created_at"]
    }

# Dashboard route
@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    username = None
    distress_count = 0
    suggestions = []
    scores = []
    labels = []
    average_score = 0
    distress_percentage = 0

    if request.method == "POST":
        username = request.form.get("username").strip().lstrip("@")
        max_tweets = int(request.form.get("max_tweets", 5))  # Default to 5 if not provided
        if username:
            tweets = fetch_user_tweets(username, max_tweets=max_tweets)
            if tweets:
                report = [analyze_post(tweet) for tweet in tweets]
                distress_count = sum(1 for result in report if result.get("alert") == "Potential distress detected")
                scores = [result["compound_score"] for result in report]
                labels = [result["sentiment"] for result in report]
                average_score = sum(scores) / len(scores) if scores else 0
                distress_percentage = (distress_count / len(report)) * 100 if report else 0
                if distress_count >= DISTRESS_THRESHOLD:
                    suggestions = [
                        "Consider reaching out to a friend or family member for support.",
                        "Take a break and engage in a relaxing activity like walking or reading.",
                        "Contact a mental health professional or helpline (e.g., 988 in the US).",
                        "Practice deep breathing or mindfulness to manage stress."
                    ]
            else:
                report = [{
                    "text": f"No tweets found for @{username} or invalid username",
                    "alert": "Error",
                    "sentiment": "N/A",
                    "compound_score": 0.0,
                    "flagged_keywords": [],
                    "entities": [],
                    "keywords": [],
                    "id": None,
                    "created_at": None
                }]

    return render_template(
        "index.html",
        report=report,
        username=username,
        distress_count=distress_count,
        threshold=DISTRESS_THRESHOLD,
        suggestions=suggestions,
        scores=scores,
        labels=labels,
        average_score=average_score,
        distress_percentage=distress_percentage
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
