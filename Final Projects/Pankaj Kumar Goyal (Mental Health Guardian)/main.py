# Importing necessary libraries
import nltk
from nltk.tokenize import word_tokenize                 # for tokenizing text into words
from nltk.corpus import stopwords                       # for getting the stopwords list in english
from nltk.stem import WordNetLemmatizer                 # for lemmatizing words
from nltk.sentiment import SentimentIntensityAnalyzer   # for sentiment analysis
import spacy                                            # for named entity recognition


# Function to check and download NLTK resources
def ensure_nltk_resource(resource, name):
    try:
        nltk.data.find(resource)
        # print(f"'{name}' is already downloaded.")
    except LookupError:
        # print(f"'{name}' not found. Downloading now...")
        nltk.download(name)


# Check and download required NLTK dependencies
ensure_nltk_resource('tokenizers/punkt', 'punkt')       # for tokenization
ensure_nltk_resource('corpora/stopwords', 'stopwords')  # for stopwords
ensure_nltk_resource('corpora/wordnet', 'wordnet')      # for lemmatization



# Initialize tools with error handling
try:
    nlp = spacy.load('en_core_web_md')                  # load the medium-sized English model
    # print("'en_core_web_md' loaded successfully.")
except OSError:
    print("Error: 'en_core_web_md' not found. Please run 'python -m spacy download en_core_web_md'.")
    exit(1)


# Initialize tools
stopwords = set(stopwords.words('english'))             # get the stopwords list in English
lemmatizer = WordNetLemmatizer()                        # initialize the WordNet lemmatizer
sia = SentimentIntensityAnalyzer()                      # initialize the SentimentIntensityAnalyzer


# Sample posts (from previous response)
posts = [
    "Can't sleep again. Work is killing me, and I feel so trapped in this city. Seattle's rain doesn't help.",
    "I'm so happy today! Just got a promotion at Tesla and celebrated with friends in LA.",
    "Why does everything feel so empty? I hate my job, and being alone in Chicago sucks.",
    "Stressed out from exams. I'm exhausted and just want this semester to end. Help.",
    "Another night of feeling worthless. I don't know how to keep going in this depressing town.",
    "Panic attacks hit me hard today at the NYC subway. I'm tired of this anxiety ruling my life.",
    "Loving this sunny day in Miami! Feeling good for once, no stress, just vibes.",
    "I'm so done with people. Angry all the time lately, and Texas heat isn't helping."
]

# Mental health concern keywords
concern_keywords = {
    "stress", "stressed", "hate", "hated", "depressing", "depressed", "sad", "angry",
    "anxious", "worried", "scared", "alone", "lonely", "isolated", "down", "miserable",
    "hopeless", "tired", "exhausted", "overwhelmed", "frustrated", "mad", "nervous",
    "empty", "numb", "lost", "despair", "failure", "worthless", "guilty", "ashamed",
    "tense", "burnout", "pressure", "sick", "fedup", "bleak", "panic", "terrified",
    "useless", "drained", "weak", "trapped", "help", "end", "die", "crisis"
}




def analyze_post(post, threshold=0.05):
    """
    Analyse the post 
    """
    # Tokenize, lemmatize, and remove stopwords
    tokens = word_tokenize(post.lower())
    cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens
                        if token.isalnum() and token not in stopwords]
    
    # Check for concern keywords
    keywords = cleaned_tokens
    flagged_keywords = [kw for kw in keywords if kw in concern_keywords]

    # Extract named entities using spacy
    doc = nlp(post)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Sentiment analysis
    sentiment = sia.polarity_scores(post)
    sentiment_label = "Positive" if sentiment['compound'] > threshold else \
                      "Negative" if sentiment['compound'] < -threshold else "Neutral"

    # Check for mental health flags
    alert = "Potential distress detected" if (sentiment['compound'] < -threshold and flagged_keywords) else "None"

    return {
        "keywords": keywords,
        "flagged_keywords": flagged_keywords,
        "entities": entities,
        "sentiment": sentiment_label,
        "compound_score": sentiment['compound'],
        "alert": alert
    }

if __name__ == '__main__':
    print(f"\n\n{'-'*50}\n\n")
    # while True:
    for post in posts:
        # print(f"\n\n{'-'*50}\n\n")
        
        # post = input("Enter a post to analyze (or type 'exit' to stop): ")
        # if post.lower() == 'exit':
        #     print("Exiting program.")
        #     break
        
        result = analyze_post(post)
        print(f"\nPost: {post}\n")
        print(f"- Keywords: {', '.join(result['keywords'])}")
        print(f"- Flagged Concern Keywords: {', '.join(result['flagged_keywords']) if result['flagged_keywords'] else 'None'}")
        print(f"- Entities: {result['entities']}")
        print(f"- Sentiment: {result['sentiment']} (compound: {result['compound_score']:.4f})")
        print(f"- Alert: {result['alert']}\n")

        print(f"\n\n{'-'*50}\n\n")