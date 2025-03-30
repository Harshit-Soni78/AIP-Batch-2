# Plant-disease-detection 

## 📌 Overview
This Flask-based web app uses a deep learning model to detect and classify diseases in leaves. It identifies  Scab, Black Rot, and healthy, providing treatment recommendations and prevention tips for each disease. Users can upload leaf images, and the system returns real-time predictions with confidence scores. Built with TensorFlow/Keras for the AI model and OpenCV for image processing, it offers an easy-to-use interface for farmers and gardeners to diagnose and manage apple tree diseases efficiently.

---

## 🚀 Features
🍃 Image Classification: Upload leaf images for disease detection

🔍 Three Disease Detection:

1. apple Scab
2. Black Rot
3. healthy

💊 Treatment Recommendations: Detailed remedies and prevention tips

📊 Confidence Scores: Shows prediction probabilities

🛡️ Bias Correction: Advanced algorithms to prevent model bias

---

## 🛠️ Technologies Used


- **Flask** (Web framework for backend)
- **TensorFlow & Keras** (Deep learning model training & inference)
- **OpenCV** (cv2) (Image processing & preprocessing)
- **NumPy** (Numerical computations)
- **Matplotlib** (Visualization during training)
- **Google Colab** (Model experimentation)
---

## 📂 Project Structure
```
📁 Plant disease detection
├── static/  
│   ├── uploads/          # User-uploaded images  
│   └── css/              # Stylesheets  
├── templates/  
│   └── index.html        # Main interface  
├── models/  
│   └── apple_model.h5    # Trained AI model  
├── app.py                # Flask application  
└── README.md  
```

---

## ⚙️ Installation & Setup

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/apple-leaf-disease-detector.git  
cd apple-leaf-disease-detector  
```

### 🔹 Step 2: Set up virtual environment
```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
.\venv\Scripts\activate   # Windows
```

### 🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Application
```bash
python app.py
```
- Open your browser and visit: **http://127.0.0.1:5000**

---

## 🚨 How It Works
 
This application combines computer vision and deep learning to analyze apple leaf images and detect diseases with high accuracy. Here's the step-by-step workflow:

1️⃣ **Image Upload**
Users upload a photo of an apple leaf through the web interface. The system accepts JPG, PNG, or JPEG formats.

2️⃣ **Preprocessing Pipeline**
The uploaded image goes through several transformation steps:

1. Color Correction: Converts from BGR to RGB format
2. Resizing: Standardizes to 224×224 pixels
3. Normalization: Scales pixel values to 0-1 range
4. CLAHE Enhancement: Improves contrast (optional based on training)

3️⃣ **Deep Learning Analysis**
Our custom-trained CNN model processes the image through:

Input (224×224×3) → 
[Conv2D → BatchNorm → ReLU → MaxPooling] × 3 → 
Flatten → Dense(256) → Dropout → 
Output(3) with Softmax
The model outputs probabilities for three classes:

1. apple Scab
2. Black Rot
3. Healthy

4️⃣ **Result Interpretation**
The system:

1. Identifies the disease with highest probability
2. Calculates confidence percentage
3. Retrieves treatment recommendations from knowledge base
4. Presents results in easy-to-understand format

📊 Technical Architecture

## graph TD
    A[User Uploads Image] --> B[Flask Server]
    B --> C[OpenCV Preprocessing]
    C --> D[TensorFlow Model]
    D --> E[Disease Prediction]
    E --> F[Remedies Database]
    F --> G[Results Page]
🧠 Model Training Details

1. Dataset: 1,000+ labeled leaf images
2. Training: 30 epochs with early stopping
3. Accuracy: 92.4% on validation set
4. Augmentation: Random rotations, flips, brightness adjustments

🌱 Real-World Application
## Farmers can use this system to:

- Detect diseases early before visible symptoms
- Reduce unnecessary pesticide use through targeted treatment 
- Learn organic prevention methods 
- Monitor orchard health over time

🔄 Continuous Improvement
## The model improves through:

- User feedback mechanism
- Periodic retraining with new data
- Community contributions of verified samples  


🚨 Limitations
## For best results:

- Use clear, well-lit photos
- Capture entire leaf when possible
- Avoid damaged or overlapping leaves
- Results are indicative - consult an agronomist for severe cases

---

## 💡 Future Enhancements

**Advanced Model Capabilities**
- Multi-Plant Support: Expand detection to cover rare crops, ornamental plants, and trees.
- Early-Stage Detection: Improve model sensitivity to identify diseases at pre-symptomatic stages.
- 3D Leaf Analysis: Integrate 3D imaging for more accurate disease localization.

**User Experience**
- Augmented Reality (AR) Overlays: Highlight infected areas on live camera feeds.
- Multilingual Support: Add localization for farmers in regional languages.
- Voice-Based Queries: Integrate voice assistants (e.g., "How to treat tomato blight?")

---

## 🤝 Contributions
Feel free to fork this repo, create issues, or submit pull requests.

---

## 📧 Contact
For any questions, reach out to **gbgarvit78@gmail.com** or open an issue on GitHub.

---

