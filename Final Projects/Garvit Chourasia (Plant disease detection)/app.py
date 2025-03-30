from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = load_model('models/apple_model.h5')
class_names = {0: "Apple Scab", 1: "Apple Black Rot", 2: "Healthy"}

disease_remedies = {
    "Apple Scab": {
        "description": "Fungal disease causing dark, scaly lesions on leaves and fruit",
        "remedies": ["Apply fungicides containing myclobutanil or sulfur", "Remove infected leaves"],
        "prevention": "Plant resistant varieties, avoid overhead watering"
    },
    "Apple Black Rot": {
        "description": "Fungal disease causing concentric rings on fruit and leaf spots",
        "remedies": ["Apply fungicides with captan", "Prune infected branches"],
        "prevention": "Proper sanitation, remove dead wood"
    },
    "Healthy": {
        "description": "No signs of disease detected",
        "remedies": [],
        "prevention": "Maintain good plant health practices"
    }
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None: return None
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224,224))
        img = img.astype('float32') / 255.0
        return np.expand_dims(img, axis=0)
    except: return None

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file selected")
            
        file = request.files['file']
        if not file or file.filename == '':
            return render_template('index.html', error="No file selected")
            
        if not allowed_file(file.filename):
            return render_template('index.html', error="Invalid file type")
            
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        processed = preprocess_image(filepath)
        if processed is None:
            return render_template('index.html', error="Invalid image file")
        
        preds = model.predict(processed)[0]
        class_idx = np.argmax(preds)
        disease_info = disease_remedies.get(class_names[class_idx], {})
        
        return render_template('index.html',
            result={
                'class': class_names[class_idx],
                'confidence': f"{preds[class_idx]*100:.1f}%",
                'description': disease_info.get('description', ''),
                'remedies': disease_info.get('remedies', []),
                'prevention': disease_info.get('prevention', '')
            },
            image_to_show=filename
        )
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
