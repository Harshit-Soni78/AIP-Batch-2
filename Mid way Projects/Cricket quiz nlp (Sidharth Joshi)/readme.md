### 🏏 **IPL & Cricket Quiz Game - README**

---

### 📌 **Project Description**
The **IPL & Cricket Quiz Game** is an interactive Python-based quiz application that tests users' knowledge of cricket and the Indian Premier League (IPL). The project uses **Natural Language Processing (NLP)** techniques like tokenization and lemmatization to normalize answers, ensuring minor variations in the player's input (e.g., "CSK" vs. "csk") are recognized as correct. 

---

### 🚀 **Features**
✅ **Multiple Levels:**  
- Level 1: Basic Cricket Trivia  
- Level 2: IPL Expert-Level Questions  

✅ **Heart & Score System:**  
- Players start with **5 hearts** and lose one for each incorrect or invalid answer.  
- Scores increase for every correct answer.  

✅ **NLP-based Answer Matching:**  
- Utilizes **NLTK's tokenizer and lemmatizer** to normalize answers, making the game smarter by handling minor variations.  

✅ **Randomized Questions:**  
- Questions are shuffled for variety in each game session.  

✅ **Final Score Summary:**  
- Displays the total score, accuracy percentage, and a performance message at the end of the game.  

---

### ⚙️ **Installation Instructions**
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd cricket-quiz
   ```

2. **Install Dependencies:**
   Install the required libraries using `pip`:
   ```bash
   pip install nltk
   ```

3. **Download NLTK Packages:**
   The game requires **'punkt'** and **'wordnet'** NLTK models:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

---

### 🛠️ **How to Run**
1. Make sure both `main.py` and `questions.py` are in the same directory.  
2. Run the game:
   ```bash
   python main.py
   ```
3. Follow the prompts to select the quiz level and answer the questions.

---

### 📄 **File Structure**
```
/cricket-quiz  
 ├── main.py                  # Main script to run the quiz  
 ├── questions.py             # Contains cricket quiz questions  
 ├── README.md                # Project documentation  
 ├── requirements.txt         # Dependencies  
```

---

### 🔥 **Technologies Used**
- **Python**: Core programming language.  
- **NLTK (Natural Language Toolkit)**: Used for tokenization and lemmatization.  
- **Random Module**: To shuffle the questions.  

---

### 🎯 **Future Enhancements**
- ✅ Add more levels with diverse difficulty.  
- ✅ Introduce a timer for each question.  
- ✅ Improve UI with a graphical interface using **Tkinter** or **PyQt**.  
- ✅ Add support for multiplayer quiz sessions.  

---

### 💡 **How to Contribute**
1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature/new-feature
   ```
3. Make your changes and commit:  
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the changes:  
   ```bash
   git push origin feature/new-feature
   ```
5. Submit a pull request.  

---

### 🏅 **Author**
- **Sidharth Joshi**  
- 📧 [Email](mailto:sidharth.joshi@example.com)  
- 🌐 [GitHub](https://github.com/sidharthjoshi)

---

✅ **Enjoy the IPL & Cricket Quiz Game and test your cricket knowledge!** 🏏