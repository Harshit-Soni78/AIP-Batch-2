import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load extracted features
X_train = np.load("data/X_train_features.npy")
X_test = np.load("data/X_test_features.npy")
y_train = np.load("data/preprocessed/y_train.npy")
y_test = np.load("data/preprocessed/y_test.npy")

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Ensure the models directory exists
os.makedirs("models", exist_ok=True)

# Save the trained model
joblib.dump(clf, "models/random_forest_model.pkl")

# Print results
print(f"Accuracy: {accuracy:.4f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)
