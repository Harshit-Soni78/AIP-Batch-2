from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
try:
    model = tf.keras.models.load_model("CNN/waste_classifier.h5")  # Ensure the path is correct
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

# Class Labels
class_labels = ['e-waste', 'glass', 'metal', 'organic', 'paper', 'plastic']

# Upload folder
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to predict image class
def predict_image(image_path):
    try:
        img_size = (224, 224)
        img = load_img(image_path, target_size=img_size)  # Load and resize the image
        img_array = img_to_array(img)  # Convert image to array
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = preprocess_input(img_array)  # Preprocess the image for MobileNetV2

        predictions = model.predict(img_array)  # Make predictions
        predicted_class = class_labels[np.argmax(predictions)]  # Get the class with the highest probability
        confidence = float(np.max(predictions))  # Get the confidence score
        return predicted_class, confidence
    except Exception as e:
        raise ValueError(f"Error during prediction: {str(e)}")

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and prediction
@app.route('/classify', methods=['POST'])
def classify():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    try:
        file.save(file_path)  # Save the uploaded file
        predicted_class, confidence = predict_image(file_path)  # Predict the class
        return jsonify({'result': f'Your waste is classified as {predicted_class} with confidence {confidence:.2f}.'})
    except Exception as e:
        return jsonify({'error': f'Failed to classify image: {str(e)}'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)