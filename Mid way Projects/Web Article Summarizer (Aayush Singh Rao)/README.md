# **Web Article Summarizer**

## **📌 Project Overview**
This Python project fetches and summarizes text from a given URL using **Natural Language Processing (NLP)** with `NLTK` and `BeautifulSoup`. It extracts key sentences based on word frequency to generate a concise summary.

## **🚀 Features**
- Extracts article text from any URL
- Tokenizes text into sentences and words
- Removes stopwords for better accuracy
- Computes word frequency for sentence importance
- Generates a summary with the most relevant sentences

## **🛠️ Installation**
Ensure you have Python installed, then install the required dependencies:

```sh
pip install requests beautifulsoup4 nltk
```

## **📜 How It Works**
1. Fetches article text using `requests` and `BeautifulSoup`.
2. Tokenizes text into sentences and words.
3. Removes stopwords and calculates word frequency.
4. Scores sentences based on important words.
5. Selects and returns the **top n most relevant sentences** as the summary.

## **💻 Usage**
Run the script and enter a URL:

```python
python summarizer.py
```

Or modify the script to work with a specific link:

```python
url = "https://example.com/article"
article_text = get_text_from_url(url)
summary = summarize_text(article_text, num_sentences=5)
print(summary)
```

## **🔧 Code Breakdown**
### **1️⃣ Extract Text from URL**
```python
def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return "".join([para.get_text() for para in paragraphs])
```
- Uses `requests` to fetch the webpage content.
- `BeautifulSoup` extracts paragraph (`<p>`) text.

### **2️⃣ Summarize the Text**
```python
def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))
    word_frequencies = {}
    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    max_freq = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] /= max_freq
    
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]
    
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return "".join(summary_sentences)
```

- Tokenizes text into sentences and words.
- Removes stopwords and assigns a score to each sentence.
- Selects **top-ranked** sentences for summarization.

## **📌 Example Output**
**Input URL:**
```
https://en.wikipedia.org/wiki/Artificial_intelligence
```

**Generated Summary:**
```
Artificial intelligence (AI) is a field of computer science focused on creating intelligent systems. AI includes techniques like machine learning, deep learning, and neural networks. The impact of AI has expanded into industries such as healthcare, finance, and automation.
```

## **📌 Dependencies**
- Python 3.x
- `requests` - Fetching webpage data
- `beautifulsoup4` - Parsing HTML
- `nltk` - NLP processing

## **📜 License**
This project is open-source and free to use.

---
Made By Ayush Singh Rao 🚀
✅ **Enjoy coding! Let me know if you need any modifications.** 

