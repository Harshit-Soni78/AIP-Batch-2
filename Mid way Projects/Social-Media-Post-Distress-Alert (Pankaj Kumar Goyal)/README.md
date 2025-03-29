<!-- Refined Readme.md with AI -->
# Social Media Post Distress Alert

This is a basic Python script that analyzes social media posts to detect signs of negative emotions or distress. It uses natural language processing (NLP) techniques to identify concerning keywords and sentiment, then alerts accordingly.

## Current Functionality
- **Manual Input**: Copy and paste the content of a social media post into the terminal.
- **Distress Detection**: The script checks for negative sentiment and predefined concern keywords (e.g., "stress," "sad," "hopeless") to flag potential distress.
- **Output**: Displays keywords, named entities, sentiment score, and an alert if distress is detected.

## Future Enhancements
- **Real-Time Integration**: Connect to social media APIs (e.g., Twitter/X) to analyze posts in real time by running the script on a server.
- **User Feed Improvement**: Adjust content recommendations to avoid amplifying negative emotions, prioritizing positive or neutral content.
- **Escalation Alerts**: Notify the user’s friends or support network if severe distress patterns persist.

## How to Duplicate the Project
Follow these steps to set up and run the project on your machine:

1. **Clone or Copy the Project**:
   - Copy the project folder to your local machine and open it in your preferred code editor (e.g., VS Code, PyCharm).

2. **Install Required Libraries**:
   - Install the dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
   - Download the spaCy language model:
     ```bash
     python -m spacy download en_core_web_md  
----------------------------------------------------------------



<!-- Raw Readme.md written -->


<!-- # Social Media Post distress Alert

This is just a basic script that detects the presence of any negative things in the social media posts and alerts them accordingly.

- Currently just have to copy paste the post content and it will detects the presence of any negative things in the social media posts and alerts
- In the future can integrate with social media application API and run the script on server real time to danalyse the posts regularly on real time. 
- And also improve the user feed according to it rather than shoing them more according to the recommendation system and if the case gets worse then alert the user's friends too with him.





## How to duplicate the Project
1. Copy paste the folder and open it in editor
2. Install the required libraries in the project  
` pip install -r requirements.txt`
3. Run the **main.py** file.
4. Copy paste the post content in the terminal to analyse it.  -->
