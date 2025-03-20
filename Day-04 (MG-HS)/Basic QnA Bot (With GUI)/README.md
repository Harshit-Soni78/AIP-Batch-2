# College Admission Chatbot

## Overview

The College Admission Chatbot is a natural language processing (NLP)-based chatbot that assists students with queries related to college admissions. It utilizes deep learning techniques to classify user inputs and generate appropriate responses. The chatbot is built using Python with TensorFlow/Keras for the model, NLTK for text preprocessing, and Tkinter for the graphical user interface (GUI).

## Features

- **User-friendly GUI**: Built using Tkinter for ease of interaction.
- **Natural Language Understanding**: Uses NLP techniques to process and understand user queries.
- **Machine Learning Model**: A pre-trained deep learning model is used for intent classification.
- **Customizable Responses**: Responses are stored in a JSON file and can be modified as needed.
- **Interactive Experience**: The chatbot responds in real-time, providing a conversational experience.

## Technologies Used

- **Python**: Core programming language.
- **TensorFlow/Keras**: For deep learning model loading and prediction.
- **Natural Language Toolkit (NLTK)**: For text preprocessing (tokenization and lemmatization).
- **Tkinter**: For building the chatbot GUI.
- **JSON**: For storing predefined intents and responses.
- **NumPy**: For handling numerical computations.
- **Pickle**: For saving and loading processed data (words and classes).

## Installation and Setup

### Prerequisites

Ensure that you have Python installed (preferably Python 3.7 or later). You can install the required dependencies using:

```sh
pip install numpy keras tensorflow nltk
```

### Downloading Necessary NLTK Resources

Before running the chatbot, ensure that the necessary NLTK resources are available:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

### Cloning the Repository

Clone the repository or download the project files.

```sh
git clone https://github.com/Harshit-Soni78/AIPlaneTech.git
cd "Day-4/Basic QnA Bot (With GUI)"
```

### Running the Chatbot

1. Ensure that the trained model (`chatbot_model.h5`) and necessary data files (`words.pkl`, `classes.pkl`, `admission_data.json`) are present in the respective folders.
2. Run the chatbot UI:

```sh
python chatbot_gui.py
```

## Project Structure

```
Basic QnA Bot (With GUI)/
   │── Model/
   │   ├── chatbot_model.h5      # Trained deep learning model
   │   ├── words.pkl             # Pickled processed vocabulary
   │   ├── classes.pkl           # Pickled classes for classification
   │
   │── Data/
   │   ├── admission_data.json   # JSON file containing intents and responses
   │
   │── chatbot_ui.py             # Main UI script
   │── train_chatbot.py          # Script to train the chatbot model
   │── README.md                 # Project documentation
```

## How It Works

### 1. **Preprocessing User Input**

- The user input is tokenized using NLTK.
- Lemmatization is applied to normalize words.

### 2. **Bag-of-Words Representation**

- The processed input is converted into a bag-of-words representation.
- This allows the model to understand the user’s query in numerical form.

### 3. **Predicting the Intent**

- The trained neural network model classifies the input intent.
- It outputs a probability distribution over the available intents.

### 4. **Generating a Response**

- The chatbot selects a response from the predefined responses in `admission_data.json`.
- The response is displayed in the chatbot’s GUI.

## Training the Chatbot

To retrain the chatbot with new data:

1. Modify `admission_data.json` to include new intents and responses.
2. Run the training script:

   ```sh
   python train_bot.py
   ```

3. The model will be updated and saved as `chatbot_model.h5`.

## Customization

### Adding New Responses

To add new intents and responses:

1. Open `Data/admission_data.json`.
2. Add a new intent with a unique tag, patterns (possible user inputs), and responses.

   ```json
   {
   "tag": "scholarships",
   "patterns": [
      "Tell me about scholarships",
      "Are there any scholarships available?"
   ],
   "responses": [
      "Yes, we offer various scholarships. Please visit our website for more details."
   ]
   }
   ```

3. Retrain the model using `train_chatbot.py`.

## Future Enhancements

- **Voice Input Support**: Integrating speech recognition.
- **Database Connectivity**: Fetching real-time data from a database.
- **Web-Based Interface**: Deploying as a web application.
- **Advanced NLP**: Using transformer-based models for better understanding.

## Author

**Harshit Soni**  
GitHub: [Harshit-Soni78](https://github.com/Harshit-Soni78)

---
Made with ❤️ by Harshit Soni
