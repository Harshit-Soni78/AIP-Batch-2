import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

# Define dataset paths
DATASET_PATH = "data"
CATEGORIES = ["first_print", "second_print"]
IMG_SIZE = 256  # Resize images to 256x256

def load_images():
    images = []
    labels = []
    for category in CATEGORIES:
        path = os.path.join(DATASET_PATH, category)
        label = CATEGORIES.index(category)
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            images.append(img)
            labels.append(label)
    return np.array(images), np.array(labels)

# Load dataset
X, y = load_images()
X = X / 255.0  # Normalize pixel values
X = X.reshape(-1, IMG_SIZE, IMG_SIZE, 1)  # Reshape for CNN

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data
np.save("data/preprocessed/X_train.npy", X_train)
np.save("data/preprocessed/X_test.npy", X_test)
np.save("data/preprocessed/y_train.npy", y_train)
np.save("data/preprocessed/y_test.npy", y_test)

print("Dataset loaded, preprocessed, and saved successfully.")