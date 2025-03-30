import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure Upload Folder
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

import image_processor 
import text_extractor  
import text_summarizer  

# Renders the HTML Page
@app.route("/")
def home():
    return render_template("index.html")

# Upload and Process Image
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    processed_img_path = os.path.join(app.config["PROCESSED_FOLDER"], filename)
    image_processor.image_cleaner(file_path, processed_img_path)  
    # Extract Text
    extracted_text = text_extractor.extract_text_from_image(processed_img_path)  

    return jsonify({
        "image_url": f"/processed/{filename}",
        "extracted_text": extracted_text
    })

# Summarize Extracted Text
@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.get_json()
    extracted_text = data.get("text", "")

    if not extracted_text:
        return jsonify({"error": "No text provided"}), 400

    summarized_text = text_summarizer.summarize_text_nltk(extracted_text) 

    return jsonify({"summary": summarized_text})

# Serve Processed Images
@app.route("/processed/<filename>")
def processed_file(filename):
    return send_from_directory(app.config["PROCESSED_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
