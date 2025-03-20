# Ultra Basic QnA Bot (Without GUI) 🤖

A simple Python-based Q&A chatbot that provides answers to common college admission-related questions. This bot operates via a command-line interface and uses a predefined knowledge base to respond to user queries.

## 📌 Features

- Provides answers to frequently asked college admission questions.
- Simple keyword-based matching using Python's `re` module.
- Interactive conversation with a greeting and name personalization.
- Ability to exit the bot gracefully using `goodbye`, `bye`, or `quit`.

## 🛠 Requirements

- Python 3.x

## 🚀 How to Run

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Run the bot using:

   ```bash
   python UltraBasicQnA_Bot.py
   ```

4. The bot will greet you and ask for your name.
5. Start asking questions about college admissions!

## 📖 Example Interaction

- Welcome to the College Admission Q&A Bot! I'm here to help answer your questions about the application process.
- Before we start, could you please tell me your name? John
- Nice to meet you, John! Feel free to ask me any questions about college admission.
- **You:** What is the application deadline?
- **Bot:** The deadline for CSE admission is at 31/04/2024. However, I recommend applying early to increase your chances of acceptance.
- **You:** Tell me about the canteen.
- **Bot:** The canteen offers a variety of options, including vegetarian and healthy choices...
- **You:** Goodbye
- Thanks for using the College Admission Q&A Bot, John! Have a great day.

## 🔍 How It Works

1. **Greeting & Name Input**

   - The bot welcomes the user and asks for their name.

2. **Keyword-Based Matching**

   - User inputs a question.
   - The bot scans for keywords in the question using Python's `re.search()`.
   - If a match is found, it returns the corresponding answer from the `knowledge_base` dictionary.

3. **Graceful Exit**

   - The user can type `goodbye`, `bye`, or `quit` to exit the bot.

## ⚠ Known Issues

- The bot uses simple keyword-based matching, so it may not understand complex questions.
- Some answers may be repetitive if multiple keywords are closely related.

## 🏗 Future Improvements

- Implement NLP for better question understanding.
- Add a GUI for a more interactive experience.
- Expand the knowledge base for more detailed responses.

## Author

**Harshit Soni**  
GitHub: [Harshit-Soni78](https://github.com/Harshit-Soni78)

---
Made with ❤️ by Harshit Soni
