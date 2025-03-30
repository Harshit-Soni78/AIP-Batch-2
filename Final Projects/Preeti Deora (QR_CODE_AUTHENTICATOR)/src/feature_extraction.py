import numpy as np
import cv2
import os
from skimage.feature import hog
from skimage.filters import sobel
from skimage.measure import shannon_entropy

# Load preprocessed data
X_train = np.load("data/preprocessed/X_train.npy")
X_test = np.load("data/preprocessed/X_test.npy")
y_train = np.load("data/preprocessed/y_train.npy")
y_test = np.load("data/preprocessed/y_test.npy")

def extract_features(images):
    feature_list = []
    for img in images:
        img = img.squeeze()  # Remove single channel dimension
        
        # Extract HOG features
        hog_features = hog(img, pixels_per_cell=(8, 8), cells_per_block=(2, 2), feature_vector=True)
        
        # Edge detection using Sobel filter
        edges = sobel(img)
        edge_mean = np.mean(edges)
        edge_std = np.std(edges)
        
        # Texture feature - Shannon Entropy
        entropy = shannon_entropy(img)
        
        # Combine features
        features = np.hstack([hog_features, edge_mean, edge_std, entropy])
        feature_list.append(features)
    
    return np.array(feature_list)

# Extract features from train and test sets
X_train_features = extract_features(X_train)
X_test_features = extract_features(X_test)

# Save extracted features
np.save("data/X_train_features.npy", X_train_features)
np.save("data/X_test_features.npy", X_test_features)

print("Feature extraction completed and saved successfully.")
