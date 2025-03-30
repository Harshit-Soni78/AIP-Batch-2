import re
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein

# Download necessary NLTK resources
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def preprocess_text(text):
    """Preprocess text for plagiarism detection."""
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def find_similar_sentences(sentences, threshold=0.8):
    """Find sentences with high similarity."""
    similar_pairs = []
    
    # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer(ngram_range=(2, 3), min_df=1)
    
    # Compute TF-IDF matrix for all sentences
    try:
        tfidf_matrix = vectorizer.fit_transform(sentences)
    except ValueError:
        # In case of empty sequence or all-stopwords sentences
        return []
    
    # Calculate cosine similarity between all sentence pairs
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Find similar pairs
    for i in range(len(sentences)):
        for j in range(i+1, len(sentences)):
            if cosine_sim[i][j] > threshold:
                similar_pairs.append((i, j, cosine_sim[i][j]))
    
    return similar_pairs

def check_text_similarity(text, threshold=0.7):
    """Check for internal similarity/repetition (self-plagiarism)."""
    # Break text into sentences
    sentences = sent_tokenize(text)
    
    # Preprocess sentences
    processed_sentences = [preprocess_text(s) for s in sentences if len(s.split()) > 5]
    
    # Find similar sentences
    similar_pairs = find_similar_sentences(processed_sentences, threshold)
    
    return similar_pairs, sentences

def detect_paraphrasing(text, reference_text, threshold=0.75):
    """Detect potential paraphrasing between texts."""
    # Break texts into sentences
    text_sentences = sent_tokenize(text)
    ref_sentences = sent_tokenize(reference_text)
    
    # Preprocess sentences
    processed_text = [preprocess_text(s) for s in text_sentences if len(s.split()) > 5]
    processed_ref = [preprocess_text(s) for s in ref_sentences if len(s.split()) > 5]
    
    # Check for direct matches first using Levenshtein distance
    direct_matches = []
    paraphrases = []
    
    for i, text_sent in enumerate(processed_text):
        for j, ref_sent in enumerate(processed_ref):
            # Calculate normalized Levenshtein similarity
            distance = Levenshtein.distance(text_sent, ref_sent)
            max_len = max(len(text_sent), len(ref_sent))
            if max_len == 0:
                similarity = 0
            else:
                similarity = 1 - (distance / max_len)
            
            if similarity > 0.9:  # Direct or near-direct match
                direct_matches.append((i, j, similarity))
            elif similarity > threshold:  # Potential paraphrase
                paraphrases.append((i, j, similarity))
    
    return direct_matches, paraphrases, text_sentences, ref_sentences

def check_plagiarism(text, reference_text=None):
    """
    Check for plagiarism in text.
    If reference_text is provided, compares against it.
    Otherwise, checks for self-plagiarism within the text.
    """
    report = []
    report.append("PLAGIARISM ANALYSIS REPORT\n")
    
    # Check for internal similarity if no reference text
    if not reference_text:
        similar_pairs, sentences = check_text_similarity(text)
        
        if not similar_pairs:
            report.append("No significant internal repetition or self-plagiarism detected.")
        else:
            report.append(f"Found {len(similar_pairs)} instances of repeated content:")
            
            # Sort by similarity score (highest first)
            similar_pairs.sort(key=lambda x: x[2], reverse=True)
            
            for i, (idx1, idx2, score) in enumerate(similar_pairs[:10], 1):
                report.append(f"\nSimilar pair #{i} (similarity: {score:.2f}):")
                report.append(f"  1. \"{sentences[idx1]}\"")
                report.append(f"  2. \"{sentences[idx2]}\"")
            
            if len(similar_pairs) > 10:
                report.append(f"\n...and {len(similar_pairs) - 10} more similar pairs.")
    else:
        # Compare with reference text
        direct_matches, paraphrases, text_sentences, ref_sentences = detect_paraphrasing(text, reference_text)
        
        # Report direct matches
        if direct_matches:
            report.append(f"Found {len(direct_matches)} instances of direct or near-direct copying:")
            
            for i, (text_idx, ref_idx, score) in enumerate(direct_matches[:5], 1):
                report.append(f"\nMatch #{i} (similarity: {score:.2f}):")
                report.append(f"  Your text: \"{text_sentences[text_idx]}\"")
                report.append(f"  Reference: \"{ref_sentences[ref_idx]}\"")
            
            if len(direct_matches) > 5:
                report.append(f"\n...and {len(direct_matches) - 5} more direct matches.")
        else:
            report.append("No direct copying detected.")
        
        # Report paraphrases
        if paraphrases:
            report.append(f"\nFound {len(paraphrases)} potential paraphrases:")
            
            for i, (text_idx, ref_idx, score) in enumerate(paraphrases[:5], 1):
                report.append(f"\nParaphrase #{i} (similarity: {score:.2f}):")
                report.append(f"  Your text: \"{text_sentences[text_idx]}\"")
                report.append(f"  Reference: \"{ref_sentences[ref_idx]}\"")
            
            if len(paraphrases) > 5:
                report.append(f"\n...and {len(paraphrases) - 5} more potential paraphrases.")
        else:
            report.append("\nNo potential paraphrasing detected.")
        
        # Overall assessment
        total_issues = len(direct_matches) + len(paraphrases)
        if total_issues == 0:
            report.append("\nOverall: No plagiarism detected.")
        elif len(direct_matches) > 5 or total_issues > 10:
            report.append("\nOverall: High level of similarity detected. Significant revision recommended.")
        elif len(direct_matches) > 0 or total_issues > 5:
            report.append("\nOverall: Moderate level of similarity detected. Some revision recommended.")
        else:
            report.append("\nOverall: Low level of similarity detected. Minor revision may be needed.")
    
    return "\n".join(report)
