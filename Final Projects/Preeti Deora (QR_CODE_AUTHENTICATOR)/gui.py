import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import cv2
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model

# Load trained CNN model
dl_model = load_model(r"C:\Users\Preeti Deora\Desktop\QR_Code_Authenticator\models\cnn_model.h5")
def preprocess_image(image_path):
    """Preprocess the input image for CNN model."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (256, 256))  # Resize to match model input
    image = image / 255.0  # Normalize pixel values
    image = image.reshape(1, 256, 256, 1)  # Reshape for CNN (batch_size, height, width, channels)
    return image

def classify_qr(image_path):
    """Classifies the QR code image using CNN."""
    image = preprocess_image(image_path)
    prediction = dl_model.predict(image)
    return "Genuine" if prediction[0][0] > 0.5 else "Counterfeit"

def upload_image():
    """Handles image upload and classification."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    result = classify_qr(file_path)
    if result:
        messagebox.showinfo("Result", f"The QR code is: {result}")

# GUI Setup
root = tk.Tk()
root.title("QR Code Authenticator")
root.geometry("400x300")

upload_btn = tk.Button(root, text="Upload QR Code", command=upload_image)
upload_btn.pack(pady=20)

root.mainloop()