In our chatbot project, the three model files serve distinct but interconnected roles in making the chatbot function efficiently. Here’s their significance:

---

### 1️⃣ `chatbot_model.h5` (Trained Deep Learning Model)

- **What is it?**
  - This is the main **trained neural network model** stored in the HDF5 format (`.h5`).
  - It is created using **Keras + TensorFlow** and trained on labeled intent data.
- **Why did we make it?**
  - We trained this model using input-output pairs (bag-of-words representations of user queries and their corresponding intent labels).
  - It allows the chatbot to predict **which intent** best matches a user’s query.
- **What is it doing?**
  - When a user enters a query, the chatbot converts it into a bag-of-words (BoW) format.
  - The model takes this as input and outputs probabilities for different intent classes.
  - The chatbot selects the intent with the **highest probability** to determine the response.

---

### 2️⃣ `words.pkl` (Vocabulary List)

- **What is it?**
  - A **pickled list of words** used during training.
  - Contains **all unique words** extracted from the training dataset (after lemmatization and tokenization).
- **Why did we make it?**
  - To ensure that the chatbot processes new input in the **same format** as it was trained on.
  - Prevents reprocessing of words every time the chatbot runs.
- **What is it doing?**
  - When a user enters a sentence, it is broken down into words.
  - Each word is checked against this list to form a **bag-of-words vector**.
  - This vector is then passed to the model (`chatbot_model.h5`) for intent prediction.

---

### 3️⃣ `classes.pkl` (Intent Labels)

- **What is it?**
  - A **pickled list of intent labels** corresponding to different categories in the dataset.
- **Why did we make it?**
  - To store the **intent labels** that the model was trained to recognize.
  - Ensures that the chatbot always interprets predictions in the **same order**.
- **What is it doing?**
  - The model outputs probabilities for different intent indices.
  - These indices are mapped back to **actual intent labels** using this file.
  - The chatbot then selects the most probable intent and retrieves a response.

---

### 🔗 How They Work Together

1. **User enters a message** → `chatbot_ui.py` preprocesses it.
2. **Bag-of-words representation** → Using `words.pkl` to match words with known vocabulary.
3. **Predict intent** → `chatbot_model.h5` predicts the most likely intent.
4. **Find intent label** → Using `classes.pkl`, the predicted class index is converted into a text label.
5. **Generate response** → The chatbot retrieves a response from `admission_data.json` based on the predicted intent.

---

This modular approach ensures that: ✅ The model is efficient and doesn’t need retraining every time.  
✅ The chatbot maintains consistency in predictions and responses.  
✅ The system is scalable—new intents can be added without breaking the structure.
