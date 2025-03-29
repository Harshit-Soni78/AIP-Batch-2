
# Climate Crisis Voice Amplifier

## What Is It?
The **Climate Crisis Voice Amplifier** is a Python-based Natural Language Processing (NLP) tool that analyzes texts about climate change—think social media posts, news blurbs, or community statements—from across the globe. Its mission? To spotlight voices that often go unheard in the climate conversation, like those from small island nations or marginalized regions, by identifying their locations, climate concerns, and urgency.

Imagine Tuvalu pleading about rising seas or a Kenyan village crying out for drought relief. This tool sifts through the noise, prioritizes these underrepresented perspectives, and delivers a clear, actionable summary. It’s about equity in a crisis that affects us all.

---

## Why It Matters
Climate change is a global problem, but most attention goes to big countries like the U.S. or Europe. Meanwhile, smaller places like Tuvalu, which is at risk of sinking, or rural Brazil, which faces deforestation, are often ignored. This project helps highlight their struggles.
- **Amplifying**: Boosting voices from less-covered areas.
- **Informing**: Highlighting urgent climate issues for awareness or action.
- **Empowering**: Giving data to activists, researchers, or policymakers.

---

## How It Works
The tool processes short texts using NLP techniques to:
1. **Identify Locations**: Spots where the text comes from (e.g., "Tuvalu," "Brazil") using Named Entity Recognition (NER).
2. **Pinpoint Issues**: Detects climate-related problems (e.g., "seas," "deforestation") with custom patterns.
3. **Measure Sentiment**: Gauges emotion (e.g., fear, hope) via sentiment analysis.
4. **Assess Urgency**: Flags urgent pleas (e.g., "threaten," "killing") and scores them.
5. **Prioritize**: Weights underrepresented regions higher to amplify their voices.

### Example
- **Input**: "Rising seas threaten russia!"
- **Output**: 
  - Location: russia
  - Priority: Urgent
  - Issue: seas
  - Sentiment: -0.38 (negative)
  - Urgency Marker: threaten
  - Score: 1.02

---

## Tech Stack
- **Python**: 3.7+
- **SpaCy**: For NER, tokenization, and custom entity patterns.
- **NLTK**: For sentiment analysis, tokenization, lemmatization, and stopwords.

---



### Installation Steps
1. **Get the Code**:
   - Clone or download this project to your machine.
   ```bash
   git clone <repository-url>
   cd climate-crisis-voice-amplifier
   ```
----------------------------------------------------------------

## How to Duplicate the Project
Follow these steps to set up and run the project on your machine:

1. **Clone or Copy the Project**:
   - Copy the project folder to your local machine and open it in your preferred code editor (e.g., VS Code, PyCharm).

2. **Install Required libraries**:
   - Open a terminal and run:
     ```bash
     pip install spacy
     pip install nltk
     python -m spacy download en_core_web_sm
     ```
----------------------------------------------------------------






