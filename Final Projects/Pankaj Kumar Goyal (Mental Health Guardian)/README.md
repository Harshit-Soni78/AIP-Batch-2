# Mental Health Guardian

## 📌 Overview
The **Mental Health Guardian** project is a proactive web application designed to analyze social media activity to detect potential signs of emotional distress. It leverages **Natural Language Processing (NLP)** techniques and **Twitter/X API** integration to assess sentiment, identify concerning language patterns, and recognize crisis-related keywords.

The tool provides actionable insights through an intuitive dashboard, including **sentiment visualizations, risk-level assessments, and support recommendations**, enabling early intervention for mental health awareness.

---

## 🚀 Features
- **Scrape social media posts** using APIs and web scraping.
- **Perform sentiment analysis** using NLTK's VADER and spaCy.
- **Detect distress-related keywords** using a predefined list.
- **User-friendly Flask web interface** for testing.

---

## 🛠️ Technologies Used
- **Flask** (Web Framework)
- **NLTK & spaCy** (NLP Processing)
- **Tweepy** (Twitter/X API for fetching posts)
- **Python-dotenv** (Environment variable management)

---

## 📂 Project Structure
```
📁 Mental Health Guardian
│── app.py                # Main Flask application
│── requirements.txt       # Required dependencies
│── templates/
│   ├── index.html         # Web UI for input and results
│── static/
│   ├── style.css          # Stylesheets
│── .env                   # API keys & environment variables
│── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/mental-health-guardian.git
cd mental-health-guardian
```

### 🔹 Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
conda create -n meantalenv  # Create a virtual environment
conda activate meantalenv  # Activate
```

### 🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Step 4: Download Required NLP Models
```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("vader_lexicon")
```
```bash
python -m spacy download en_core_web_sm
```

### 🔹 Step 5: Set Up API Keys (Twitter, Twilio, Telegram)
Create a `.env` file in the project root and add:
```env
BEARER_TOKEN = your_bearer_token
```

---

## ▶️ Running the Application
```bash
python app.py
```
- Open your browser and visit: **http://127.0.0.1:5000/**

---

## 🚨 How It Works
1. The user enters or scrapes a social media post.
![Screenshot 2025-03-30 005103](https://github.com/user-attachments/assets/a5b1aa2d-2441-4115-9387-182f27aa1188)

2. The system tokenizes the text, removes stopwords, and lemmatizes words.
3. **Sentiment Analysis** is performed using **NLTK’s VADER**.
4. If the post contains **distress keywords** (e.g., "depressed", "hopeless", "suicidal"), an alert is triggered.
![Screenshot 2025-03-30 005232](https://github.com/user-attachments/assets/255b21ed-d820-4df7-976e-d2440fffe62c)
![Screenshot 2025-03-30 005256](https://github.com/user-attachments/assets/7e9b2329-c45d-4f42-94ea-662af6c86af4)
![Screenshot 2025-03-30 005322](https://github.com/user-attachments/assets/aff24392-8f9a-401f-9228-d0f046592f48)



---

## 📜 Example Distress Keywords
```python
concern_keywords = {
    "stress", "stressed", "depressed", "anxious", "hopeless", "miserable",
    "alone", "numb", "worthless", "failure", "despair", "scared",
    "burnout", "trapped", "useless", "end", "die", "crisis", "help"
}
```

---

## 📌 API Integration Details
- **Twitter/X API**: Fetch user tweets using Tweepy.
- Sign up on the X Developer Portal and get the bearer token after creating a project.
- Free-tier has limited requests, but higher quotas are available in premium and paid plans.

---

## 💡 Future Enhancements
- **Send alerts via social media DMs.**
- **Implement machine learning models** for more accurate distress detection.
- **Add real-time monitoring** for multiple social media platforms.
- **Introduce user authentication** and dashboard for tracking alerts.
- **Use Deep Learning (BERT, GPT-4)** for enhanced sentiment analysis.

---

## 🤝 Contributions
Feel free to fork this repo, create issues, or submit pull requests.

---

## 📧 Contact
For any questions, reach out to **pankajgoyal4152@gmail.com** or open an issue on GitHub.

---

