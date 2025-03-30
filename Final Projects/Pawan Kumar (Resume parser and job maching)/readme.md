## Resume parser and job Matcher


##  Overview
Resume Matcher is a Python-based tool that extracts key details from resumes (PDF/DOCX) and evaluates their compatibility with a given job description. It uses NLP techniques for information extraction and TF-IDF with cosine similarity for job matching.

## Features

- **Extracts resume text** from PDF and DOCX files.
- **Identifies Education, Experience, and Skills** using NLP and keyword matching.
- **Matches resume against job descriptions** using TF-IDF and cosine similarity.
- **Provides a Job Match Score (%)** to evaluate relevance.

## installation

!pip install spacy pdfplumber docx2txt scikit-learn
!python -m spacy download en_core_web_sm

## ussage
 run the python code in python environment
 ```
 Resume parser and job Matcher code

 ```
 -Enter the resume file path (PDF/DOCX) and job description when prompted.



## How It Works (in code)

import spacy, pdfplumber, docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Function to extract text from PDF or DOCX resumes
def extract_text(file_path):
    """Extracts text from a PDF or DOCX file, removing unnecessary whitespace."""
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_path.endswith(".docx"):
        text = docx2txt.process(file_path)
    else:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

# Function to process extracted text and identify relevant information
def process_resume(text):
    """Extracts structured information like skills, education, and experience using NLP and keyword matching."""
    doc = nlp(text)
    extracted_info = {"Education": [], "Experience": [], "Skills": []}
    
   # Extract Education & Experience using Named Entity Recognition
    for ent in doc.ents:
        if ent.label_ in ["EDUCATION", "ORG"]:   # Organizations like universities
            extracted_info["Education"].append(ent.text)
        elif ent.label_ in ["DATE", "TIME"]:     # Dates indicating experience periods
            extracted_info["Experience"].append(ent.text)
    
   # Extract Skills using keyword matching
    skill_keywords = {"python", "java", "c++", "machine learning", "data science", "nlp", "tensorflow", "keras", "sql", "react", "django", "flask", "cloud computing"}
    extracted_info["Skills"] = list(set(word.text.lower() for word in doc if word.text.lower() in skill_keywords))
    
    return {key: ", ".join(set(value)) if value else "Not detected" for key, value in extracted_info.items()}

# Function to compare resume with job description
def match_job(resume_text, job_desc):
    """Enhances matching accuracy using TF-IDF with domain-specific stopword removal and bigrams."""
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    return round(cosine_similarity(vectors[0], vectors[1])[0][0] * 100, 2)

if __name__ == "__main__":
   # Load spaCy NLP model
    nlp = spacy.load("en_core_web_sm")
    
   # Get user input for resume file path and job description
    file_path = input("Enter resume file path (PDF/DOCX): ").strip()
    job_desc = input("Enter job description: ").strip()
    
   # Extract, process, and match resume with job description
    resume_text = extract_text(file_path)
    resume_info = process_resume(resume_text)
    match_score = match_job(resume_text, job_desc)
    
   # Display results
    print("\n Resume Details:")
    for label, value in resume_info.items():
        print(f"{label}: {value}")
    
    print(f"\n Job Match Score: {match_score}%")


1. **Text Extraction**: Reads and cleans text from the given resume file.
2. **NLP Processing**: Uses spaCy's `en_core_web_sm` model to detect entities.
3. **Information Extraction**:
   - Education: Identifies institutions and degrees.
   - Experience: Detects timeframes.
   - Skills: Matches against a predefined skill list.
4. **Job Matching**:
   - Converts resume & job description into TF-IDF vectors.
   - Computes similarity score using cosine similarity.
   - Outputs a percentage score indicating relevance.

## Example Output
```
 Resume Details:
Education: XYZ University, Bachelor of Computer Science
Experience: 3 years experience
Skills: python, machine learning, tensorflow

 Job Match Score: 85.75%
```
## Use Cases

Job Seekers: Optimize resumes to match job descriptions.

Recruiters: Quickly assess candidate relevance for job roles.

HR Teams: Automate initial resume screening processes.









## Author

**Pawan Kumar**
GitHub: [Kpawankumar][https://github.com/Kpawankumar]
