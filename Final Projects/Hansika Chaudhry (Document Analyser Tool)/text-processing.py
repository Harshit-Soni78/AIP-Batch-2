import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from textblob import TextBlob
from transformers import pipeline

# Download necessary NLTK resources
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

def clean_text(text):
    """Clean text by removing extra whitespace, special characters, etc."""
    # Remove special characters and digits
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def generate_summary(text, ratio=0.3):
    """Generate a summary of the input text using extractive summarization."""
    # For long documents, use transformer-based summarization
    if len(text) > 10000:
        return generate_transformer_summary(text)
    
    # Clean the text
    cleaned_text = clean_text(text)
    
    # Tokenize sentences
    sentences = sent_tokenize(cleaned_text)
    
    # Skip summarization for very short texts
    if len(sentences) <= 5:
        return text
    
    # Tokenize words and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(cleaned_text.lower())
    words = [word for word in words if word not in stop_words]
    
    # Calculate word frequency
    freq_dist = FreqDist(words)
    
    # Score sentences based on word frequency
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if i not in sentence_scores:
                    sentence_scores[i] = 0
                sentence_scores[i] += freq_dist[word]
    
    # Normalize sentence scores
    for i in sentence_scores:
        sentence_scores[i] = sentence_scores[i] / len(word_tokenize(sentences[i]))
    
    # Select top sentences
    num_sentences = max(3, int(len(sentences) * ratio))
    top_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    top_indices = sorted(top_indices)  # Sort by original order
    
    # Combine selected sentences
    summary = " ".join([sentences[i] for i in top_indices])
    
    return summary

def generate_transformer_summary(text, max_length=150):
    """Generate summary using transformer models for longer texts."""
    summarizer = pipeline("summarization")
    
    # Split into chunks if too long
    max_chunk_length = 1024
    chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    summaries = []
    for chunk in chunks:
        if len(chunk) < 50:  # Skip very small chunks
            continue
        summary = summarizer(chunk, max_length=max_length, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    return " ".join(summaries)

def analyze_sentiment(text):
    """Analyze sentiment and tone, with focus on risks, obligations, and penalties."""
    # Basic sentiment analysis
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Look for concerning terms
    risk_terms = ['risk', 'liability', 'penalty', 'terminate', 'breach', 'damage', 'fault', 
                 'failure', 'obligation', 'responsible', 'legal action', 'sue', 'lawsuit']
    
    obligation_terms = ['must', 'shall', 'required', 'obligation', 'duty', 'responsible', 
                        'mandatory', 'obligated', 'bound', 'compulsory']
    
    penalty_terms = ['penalty', 'fine', 'fee', 'forfeit', 'compensation', 'damages', 
                    'punishment', 'consequence', 'termination', 'liability']
    
    # Find sentences containing these terms
    sentences = sent_tokenize(text)
    risk_sentences = []
    obligation_sentences = []
    penalty_sentences = []
    
    for sentence in sentences:
        lower_sentence = sentence.lower()
        
        if any(term in lower_sentence for term in risk_terms):
            risk_sentences.append(sentence)
            
        if any(term in lower_sentence for term in obligation_terms):
            obligation_sentences.append(sentence)
            
        if any(term in lower_sentence for term in penalty_terms):
            penalty_sentences.append(sentence)
    
    # Generate the analysis report
    report = []
    report.append(f"SENTIMENT ANALYSIS REPORT\n")
    report.append(f"Overall Sentiment: {'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'}")
    report.append(f"Sentiment Score: {polarity:.2f} (-1 to +1)")
    report.append(f"Subjectivity: {subjectivity:.2f} (0 = factual, 1 = subjective)")
    report.append("\n")
    
    report.append("RISK ANALYSIS\n")
    if risk_sentences:
        report.append(f"Found {len(risk_sentences)} sentences with potential risks:")
        for i, sentence in enumerate(risk_sentences[:10], 1):  # Limit to 10 examples
            report.append(f"{i}. {sentence}")
        if len(risk_sentences) > 10:
            report.append(f"...and {len(risk_sentences) - 10} more.")
    else:
        report.append("No significant risk terms detected.")
    report.append("\n")
    
    report.append("OBLIGATION ANALYSIS\n")
    if obligation_sentences:
        report.append(f"Found {len(obligation_sentences)} sentences with obligations:")
        for i, sentence in enumerate(obligation_sentences[:10], 1):
            report.append(f"{i}. {sentence}")
        if len(obligation_sentences) > 10:
            report.append(f"...and {len(obligation_sentences) - 10} more.")
    else:
        report.append("No significant obligation terms detected.")
    report.append("\n")
    
    report.append("PENALTY ANALYSIS\n")
    if penalty_sentences:
        report.append(f"Found {len(penalty_sentences)} sentences with penalties or consequences:")
        for i, sentence in enumerate(penalty_sentences[:10], 1):
            report.append(f"{i}. {sentence}")
        if len(penalty_sentences) > 10:
            report.append(f"...and {len(penalty_sentences) - 10} more.")
    else:
        report.append("No significant penalty terms detected.")
    
    return "\n".join(report)
