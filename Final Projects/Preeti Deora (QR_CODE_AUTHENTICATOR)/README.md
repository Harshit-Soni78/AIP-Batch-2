# QR Code Authentication: A Machine Learning and Deep Learning Approach

## Project Overview
This project aims to authenticate QR codes using both traditional machine learning (ML) models and deep learning (DL) techniques. The dataset consists of genuine and counterfeit QR codes, with handcrafted feature extraction techniques applied to enhance classification.

## Directory Structure
```
QR_Code_Authentication/
│── data/                    # Store your downloaded images
│   ├── first_print/            # Original QR codes
│   ├── second_print/           # Counterfeit QR codes
│── src/                        # Source code files
│   ├── data_exploration.ipynb  # Data exploration
│   ├── preprocessing.py        # Image loading & preprocessing
│   ├── feature_extraction.py   # Extracts handcrafted features
│   ├── train_ml.py             # Traditional ML model
│   ├── train_cnn.py            # Deep learning model
│   ├── evaluate.py             # Model evaluation
│── models/                     # Saved models
│── results/                    # Logs, confusion matrices, etc.
│── gui.py                      # GUI for QR authentication
│── requirements.txt            # Required dependencies
│── README.md                   # Project overview and instructions
```

## Dataset and Preprocessing
### Dataset Structure
The dataset consists of two classes:
- **First Prints**: Original QR codes.
- **Second Prints**: Counterfeit QR codes.

#### Dataset Statistics:
- **Total First Prints:** 100
- **Total Second Prints:** 100
- **Average Mean Intensity (First Prints):** 121.61
- **Average Mean Intensity (Second Prints):** 105.16

### Preprocessing Steps
- **Grayscale Conversion**: QR codes are converted to grayscale to remove unnecessary color information.
- **Resizing**: Images are resized to **256×256** pixels for model compatibility.
- **Normalization**: Pixel values are scaled between 0 and 1.
- **Feature Extraction**: For the ML model, handcrafted features such as intensity distribution and edge detection are extracted.

## Feature Extraction
The project extracts handcrafted features using:
- **Histogram of Oriented Gradients (HOG)** for texture and shape analysis.
- **Sobel Filter** for edge detection, capturing edge mean and standard deviation.
- **Shannon Entropy** for texture analysis.

## Model Training & Evaluation
Both ML and CNN-based models are trained using extracted features and raw image data respectively.

### Machine Learning Model
- **Classifier Used**: Random Forest Classifier.
- **Evaluation Metrics**: Accuracy, Confusion Matrix, Precision, Recall, and F1-score.

#### Machine Learning Model Performance:
- **Accuracy:** 100%
- **Confusion Matrix:**
  ```
  [[21  0]
   [ 0 19]]
  ```
- **Classification Report:**
  ```
                precision    recall  f1-score   support
  
             0       1.00      1.00      1.00        21
             1       1.00      1.00      1.00        19
  
      accuracy                           1.00        40
     macro avg       1.00      1.00      1.00        40
  weighted avg       1.00      1.00      1.00        40
  ```

### Deep Learning Model
- **Architecture**: Convolutional Neural Network (CNN)
- **Layers**:
  - Convolutional Layers with ReLU Activation
  - Max-Pooling Layers
  - Fully Connected Layers
  - Softmax Activation for Classification
- **Loss Function**: categorical_crossentropy
- **Optimizer**: Adam

#### Deep Learning Model Performance:
- **Accuracy:** 100%
- **Confusion Matrix:**
  ```
  [[21  0]
   [ 0 19]]
  ```
- **Classification Report:** Same as ML model.

## Running the Project
### Prerequisites
Ensure you have the required dependencies installed:
```sh
pip install -r requirements.txt
```

### Steps to Execute
1. **Preprocess Images:** Run `preprocessing.py` to resize and normalize images.
2. **Extract Features:** Run `feature_extraction.py` to obtain HOG, Sobel, and entropy features.
3. **Train ML Model:** Run `train_ml.py` for traditional classification.
4. **Train CNN Model:** Run `train_cnn.py` for deep learning-based classification.
5. **Evaluate Models:** Run `evaluate.py` to assess model performance.
6. **Use GUI:** Execute `gui.py` for an interactive QR code authentication interface.

## Future Work
- **Robustness Testing**: Evaluating performance on real-world noisy QR codes.

##**Download Pretrained models**
- CNN Model:
https://drive.google.com/file/d/1qKVF7bpt6rfI07VLH3ODIZ6UmSKaeyt0/view?usp=sharing

- X_train_features.npy
https://drive.google.com/file/d/1ghkJtpSi04m1ry4-f4U0y9oWRBF1jjYD/view?usp=drive_link

- X_train.npy
https://drive.google.com/file/d/1ccVSe8A57nMAjPk67PYrFi7FvWZJYocg/view?usp=sharing









 **Model Optimization**: Experimenting with different architectures and hyperparameters.
 **Deployment**: Integrating the model into a real-time authentication system.
 **Expand dataset** for better generalization.
 **Implement real-time scanning** with mobile applications.
 **Optimize CNN architecture** for faster inference.


