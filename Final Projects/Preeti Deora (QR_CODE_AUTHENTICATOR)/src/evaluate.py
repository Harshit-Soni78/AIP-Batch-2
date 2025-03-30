import os
import numpy as np
import joblib
import tensorflow as tf
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load test data
X_test_ml = np.load("data/X_test_features.npy")
y_test = np.load("data/preprocessed/y_test.npy")
X_test_dl = np.load("data/preprocessed/X_test.npy")

# Load ML model
ml_model = joblib.load("models/random_forest_model.pkl")
y_pred_ml = ml_model.predict(X_test_ml)

# Evaluate ML model
ml_accuracy = accuracy_score(y_test, y_pred_ml)
ml_conf_matrix = confusion_matrix(y_test, y_pred_ml)
ml_class_report = classification_report(y_test, y_pred_ml)

ml_results = f"Machine Learning Model Evaluation:\n" \
             f"Accuracy: {ml_accuracy:.4f}\n" \
             f"Confusion Matrix:\n{ml_conf_matrix}\n" \
             f"Classification Report:\n{ml_class_report}\n"

# Load Deep Learning model
dl_model = tf.keras.models.load_model("models/cnn_model.h5")

# Predict with Deep Learning model
y_pred_dl = dl_model.predict(X_test_dl)
y_pred_dl = np.argmax(y_pred_dl, axis=1)  # Convert from probabilities to class labels

# Evaluate Deep Learning model
dl_accuracy = accuracy_score(y_test, y_pred_dl)
dl_conf_matrix = confusion_matrix(y_test, y_pred_dl)
dl_class_report = classification_report(y_test, y_pred_dl)

dl_results = f"\nDeep Learning Model Evaluation:\n" \
             f"Accuracy: {dl_accuracy:.4f}\n" \
             f"Confusion Matrix:\n{dl_conf_matrix}\n" \
             f"Classification Report:\n{dl_class_report}\n"

# Ensure the results directory exists
os.makedirs("results", exist_ok=True)

# Save results to a file
with open("results/evaluation_results.txt", "w") as f:
    f.write(ml_results)
    f.write(dl_results)

print(ml_results)
print(dl_results)