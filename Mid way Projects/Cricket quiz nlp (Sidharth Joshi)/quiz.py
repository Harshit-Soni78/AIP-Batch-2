import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from questions import cricket_questions

nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def normalize_answer(text):
    """Tokenize and lemmatize the answer for comparison"""
    tokens = word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(lemmatized_tokens)

def start_quiz(questions):
    """Run the quiz logic"""
    hearts = 5
    score = 0

    print("\n🏏 Welcome to the IPL & Cricket NLP Quiz 🏏")
    print(f"💖 Hearts: {hearts} | 🏅 Score: {score}")

    random.shuffle(questions)

    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}: {q['question']}")
        for i, option in enumerate(q['options'], start=1):
            print(f"{i}. {option}")

        try:
            user_input = int(input("Enter the option number: "))
            if 1 <= user_input <= len(q['options']):
                selected_answer = q['options'][user_input - 1]
            else:
                print("Invalid option! You lost a heart 💔")
                hearts -= 1
                continue
        except ValueError:
            print("Invalid input! You lost a heart 💔")
            hearts -= 1
            continue

        correct_answer = q['answer']

        # Normalize answers using NLP
        norm_user_ans = normalize_answer(selected_answer)
        norm_correct_ans = normalize_answer(correct_answer)

        if norm_user_ans == norm_correct_ans:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {correct_answer}")
            hearts -= 1

        print(f"💖 Hearts: {hearts} | 🏅 Score: {score}")

        if hearts == 0:
            print("\n😔 Game over! You're out of hearts.")
            break

    show_result(score, len(questions))

def show_result(score, total):
    """Display the final result"""
    percentage = int((score / total) * 100)
    if percentage >= 90:
        message = "🏅 IPL Expert! You're a cricket guru!"
    elif percentage >= 60:
        message = "👍 Great job! You're getting there."
    else:
        message = "📚 Keep practicing! You'll get better."

    print("\n🎯 Quiz Completed!")
    print(f"🏅 Score: {score}/{total} | 📊 Accuracy: {percentage}%")
    print(f"✨ {message}")

def main():
    """Select quiz level"""
    print("Select Quiz Level:")
    print("1. Level 1 - Basic Cricket")
    print("2. Level 2 - IPL Expert")
    
    level_choice = input("\nEnter the level number: ")
    
    if level_choice == "1":
        level = "Level 1"
    elif level_choice == "2":
        level = "Level 2"
    else:
        print("Invalid level selected. Exiting!")
        return

    start_quiz(cricket_questions[level])

if __name__ == "__main__":
    main()
