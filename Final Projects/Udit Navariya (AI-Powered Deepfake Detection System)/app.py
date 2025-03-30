import uvicorn
from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import torch
import torchvision.transforms as transforms
from fastapi.responses import JSONResponse
from PIL import Image
import io

# Initialize FastAPI
app = FastAPI()

# Load Pre-trained Deepfake Detection Model
# (Ensure the model is downloaded and placed correctly in the directory)
model_path = "deepfake_model.pth"  # Replace with actual model file
model = torch.load(model_path, map_location=torch.device('cpu'))
model.eval()

# Image Preprocessing Function
def preprocess_image(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

@app.post("/analyze")
async def analyze_file(file: UploadFile = File(...)):
    try:
        # Read file into memory
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        processed_image = preprocess_image(image)

        # Perform deepfake detection
        with torch.no_grad():
            output = model(processed_image)
            confidence = torch.sigmoid(output).item()
            is_deepfake = confidence > 0.5

        return JSONResponse(content={
            "is_deepfake": is_deepfake,
            "confidence": confidence
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
