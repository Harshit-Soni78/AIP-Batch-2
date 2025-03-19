# ******************** Ultra Basic QnA Bot (Without GUI) ********************

# importing required things from re library
# - `search` is a function which Scan through string looking for a match to the pattern, returning a Match object, or None if no match was found.
# - `IGNORECASE` is a constant Literal[RegexFlag.I]
from re import IGNORECASE, search

# Defining Knowledge database
knowledge_base = {
    "application deadline": "The application deadline is December 1st for regular decision.",
    "application requirements": "You will need to submit your transcripts, test scores, essays, and letters of recommendation.",
    "admission requirements": " The requirements vary depending on your program of interest, but generally include transcripts, test scores, essays, and letters of recommendation. You can find more specific details on the college website.",
    "application deadline": "The deadline for CSE admission is at 31/04/2024. However, I recommend applying early to increase your chances of acceptance.",
    "canteen": "The canteen offers a variety of options, including vegetarian and healthy choices. There are also several cafes and restaurants on campus if you're looking for something different.",
    "Professors": " The faculty at MIT are highly qualified and passionate about their subjects. They are generally approachable and supportive of their students.",
    "research opportunities for undergraduates": "Yes, several departments offer research opportunities for students. You can talk to your professors or department head to learn more about available options.",
    "labs": " The labs are modern and well-equipped with the latest technology. You'll have access to all the resources you need for your studies and research.",
    "Seminars and Events": " Yes, the college regularly hosts lectures, workshops, and seminars by renowned scholars and professionals. It's a great way to learn from experts and explore new ideas.",
}

# First of all we will ask user for his name
global user_info  # Store collected user information for personalization

user_info = "friend"

def greetAndAskName():
    # Welcome statement
    print("Welcome to the College Admission Q&A Bot! I'm here to help answer your questions about the application process.")
    # Ask Name
    name = input("Before we start, could you please tell me your name? ")
    global user_info
    user_info = name
    # Print Greet
    print(f"Nice to meet you, {name}! Feel free to ask me any questions about college admission.")


# Function to handle questions
def handle_question(question):
    # Searching for keyword in question
    for keyword in knowledge_base:
        # if keyword in question matches with knowledge_base
        if search(keyword, question, IGNORECASE):
            response = knowledge_base[keyword]
            return response    
    # if keyword in question does not matches with knowledge_base
    return "I'm not sure I understand that question. Could you rephrase it or try asking something different?"

# Core Functionality of Bot in a Function
def bot():
    # Greet and ask name
    greetAndAskName()
    # loop for interaction
    while True:
        question = input("You: ")
        # condition for loop break
        if question.lower() in ["goodbye", "bye", "quit"]:
            print("Thanks for using the College Admission Q&A Bot, " + user_info + "! Have a great day.")
            break
        # handle questions and print answers
        answer = handle_question(question)
        print("Bot:", answer)


# calling the Bot function
if __name__ == "__main__":
    bot()
