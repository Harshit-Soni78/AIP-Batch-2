**Project Overview:**


This project is a Resume Analyzer that takes a PDF resume as input, extracts text, and evaluates its quality using Natural Language Processing (NLP) techniques. It calculates an ATS (Applicant Tracking System) score based on the presence of important keywords and provides suggestions for improvement.



**Features:**


PDF Upload: Users can upload a resume in PDF format.

Text Extraction: Extracts text using pdfminer.six.

Preprocessing: Removes stopwords, tokenizes, and lemmatizes text.

Skill & Keyword Extraction: Identifies important entities using spaCy.

ATS Score Calculation: Evaluates how well the resume matches job requirements.

Suggestions for Improvement: Recommends ways to optimize the resume.

User Interface: Built with Streamlit for an interactive experience.


**Technologies Used:**


Python (Main language)

Streamlit (User Interface)

spaCy (NLP processing)

NLTK (Text preprocessing)

pdfminer.six (PDF text extraction)


**How It Works:**


Upload a PDF Re

Extract & Process the Text

Analyze Resume Content (Skills, Keywords, etc.)

Generate an ATS Score

Suggest Improvements
