# Twitter Sentiment Analysis 🐦📊

## Project Overview
This is a machine learning-powered web application that performs sentiment analysis on text inputs and Twitter user tweets. The project uses natural language processing techniques to classify text as positive or negative with high accuracy.

## Features ✨
- Sentiment analysis for custom text inputs
- Sentiment analysis for recent tweets from a specific Twitter user
- Machine learning model trained on 1.6 million tweets
- Interactive Streamlit web interface
- Color-coded sentiment visualization

## Technology Stack 🛠️
- Python
- Scikit-learn
- NLTK
- Streamlit
- Nitter Scraper
- Logistic Regression
- TF-IDF Vectorization

## Installation 🚀

### Prerequisites
#### Required Python Libraries
Install the following libraries using pip:
```bash
pip install:
- streamlit
- scikit-learn
- nltk
- pandas
- numpy
- re
- pickle
- ntscraper
```

#### Detailed Library Installation
```bash
pip install streamlit scikit-learn nltk pandas numpy regex ntscraper
```

#### Dataset
Download the training dataset from Kaggle:
- [Twitter Sentiment Analysis Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)

Direct Download Link:
```
https://www.kaggle.com/datasets/kazanova/sentiment140/download
```

### Setup Steps
1. Clone the repository
```bash
git clone https://github.com/yourusername/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Download NLTK resources
```python
import nltk
nltk.download('stopwords')
```

## Project Structure 📂
```
twitter-sentiment-analysis/
│
├── model.pkl             # Trained sentiment analysis model
├── vectorizer.pkl        # TF-IDF vectorizer
├── training.csv          # Dataset used for training
├── app.py                # Streamlit web application
└── requirements.txt      # Project dependencies
```

## How It Works 🔍
1. **Data Preprocessing**: 
   - Clean and normalize text
   - Remove stopwords
   - Apply Porter stemming
   - Convert text to numerical features using TF-IDF

2. **Model Training**:
   - Use Logistic Regression on 1.6 million pre-labeled tweets
   - 80/20 train-test split
   - Vectorize text features
   - Classify sentiment as positive or negative

3. **Web Interface**:
   - Two analysis modes: custom text and Twitter username
   - Real-time sentiment prediction
   - Color-coded results (Green: Positive, Red: Negative)

## Usage 💻
Run the Streamlit application:
```bash
streamlit run app.py
```

### Web Interface Options
1. **Input Text**: Directly analyze sentiment of any text
2. **Get Tweets**: Fetch and analyze sentiment of recent tweets from a Twitter user

## Model Performance 📈
- Trained on 1.6 million tweets
- High accuracy sentiment classification
- Fast real-time predictions

## Contributing 🤝
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Limitations ⚠️
- Limited to 5 tweets per user fetch
- Relies on Nitter for tweet scraping
- Sentiment analysis based on text only

## Future Improvements 🚧
- Implement more advanced NLP techniques
- Add support for multiple languages
- Improve model accuracy
- Create more detailed sentiment analysis (beyond binary classification)

## License 📄
Distributed under the MIT License. See `LICENSE` for more information.

## Contact 📧
Your Name - prajapatramesh520@gmail.com

Project Link: [https://github.com/yourusername/twitter-sentiment-analysis](https://github.com/PRAJAPATBOI/Twitter-Sentiment-Analysis)

## Dataset Citation
Sentiment140 dataset with 1.6 million tweets (Sentiment Analysis) 
Kaggle Link: https://www.kaggle.com/datasets/kazanova/sentiment140
