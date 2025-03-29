import spacy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Load SpaCy model and tools
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Add entity ruler AFTER NER
ruler = nlp.add_pipe("entity_ruler", after="ner")
patterns = [
    {"label": "CLIMATE", "pattern": "seas"},
    {"label": "CLIMATE", "pattern": "deforestation"},
    {"label": "CLIMATE", "pattern": "flood"},
    {"label": "CLIMATE", "pattern": "drought"},
    {"label": "URGENCY", "pattern": "threaten"},
    {"label": "URGENCY", "pattern": "killing"},
    {"label": "URGENCY", "pattern": "help"},
    {"label": "URGENCY", "pattern": "now"},
    {"label": "URGENCY", "pattern": "needs"}
]
ruler.add_patterns(patterns)

# Location weights
location_weights = {
    "Tuvalu": 1.5, "Kenya": 1.4, "Brazil": 1.2, "USA": 0.8, "Europe": 0.9
}

# Function to process text
def analyze_climate_text(text):
    if not text or not isinstance(text, str):
        return {"Error": "Invalid input: Text must be a non-empty string"}
    
    # Tokenize and clean
    tokens = word_tokenize(text.lower())
    cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token.isalpha()]
    print(f"Cleaned Tokens: {cleaned_tokens}")
    
    # Process with SpaCy
    doc = nlp(text.lower())  # Lowercase for consistency
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    climate_issues = [ent.text for ent in doc.ents if ent.label_ == "CLIMATE"]
    urgency_markers = [ent.text for ent in doc.ents if ent.label_ == "URGENCY"]
    print(f"Entities: {entities}")
    
    # Sentiment analysis
    sentiment = sia.polarity_scores(text)
    print(f"Sentiment: {sentiment}")
    
    # Calculate urgency score
    location = ", ".join(locations) if locations else "Unknown"
    weight = location_weights.get(locations[0] if locations else "Unknown", 1.0)
    urgency_score = (len(urgency_markers) * 0.3 + abs(sentiment["compound"])) * weight
    level = ("Urgent" if urgency_score > 0.5 else 
             "High Concern" if urgency_score > 0.3 else 
             "Notable")
    
    # Generate output
    issue_str = ", ".join(climate_issues) if climate_issues else "climate issue"
    urgency_str = ", ".join(urgency_markers) if urgency_markers else "none"
    result = {
        "Location": location,
        "Level": level,
        "Issue": issue_str,
        "Sentiment": sentiment["compound"],
        "Urgency Marker": urgency_str,
        "Score": round(urgency_score, 2)
    }
    return result

# Test
sample_texts = [
    "Rising seas threaten Tuvalu!",
    "Deforestation in Brazil is killing us.",
    "Drought in Kenya needs help now!",
    "Flood risks rise in Europe."
]

print("Climate Crisis Voice Amplifier Results:")
print("-" * 50)
for text in sample_texts:
    print(f"\nAnalyzing: {text}")
    result = analyze_climate_text(text)
    for key, value in result.items():
        print(f"{key}: {value}")
    print("-" * 50)
