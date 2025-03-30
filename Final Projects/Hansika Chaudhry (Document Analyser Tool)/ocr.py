import os
import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance

def preprocess_image(image):
    """Apply preprocessing to improve OCR accuracy."""
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Correct skew
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(rotated, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Denoise
    denoised = cv2.fastNlMeansDenoising(binary, None, 10, 7, 21)
    
    return denoised

def enhance_image(img_path):
    """Enhance image brightness, contrast for better OCR."""
    img = Image.open(img_path)
    
    # Enhance brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.2)  # Increase brightness by 20%
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)  # Increase contrast by 50%
    
    # Save temporarily
    temp_path = f"{os.path.splitext(img_path)[0]}_enhanced.jpg"
    img.save(temp_path)
    
    return temp_path

def extract_text_from_image(image_path):
    """Extract text from an image file using OCR."""
    # Enhance image
    enhanced_path = enhance_image(image_path)
    
    # Read and preprocess image
    image = cv2.imread(enhanced_path)
    processed_image = preprocess_image(image)
    
    # Save processed image for debugging if needed
    cv2.imwrite(f"{os.path.splitext(image_path)[0]}_processed.jpg", processed_image)
    
    # Perform OCR
    text = pytesseract.image_to_string(processed_image)
    
    # Clean up
    if os.path.exists(enhanced_path):
        os.remove(enhanced_path)
    
    return text

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using OCR."""
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Process each page
    text_content = []
    for i, image in enumerate(images):
        # Save image temporarily
        temp_path = f"temp_page_{i}.jpg"
        image.save(temp_path, 'JPEG')
        
        # Process the image
        page_text = extract_text_from_image(temp_path)
        text_content.append(f"--- Page {i+1} ---\n{page_text}\n")
        
        # Clean up
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    return "\n".join(text_content)

def process_document(doc_path):
    """Process document based on file type."""
    file_ext = os.path.splitext(doc_path)[1].lower()
    
    if file_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']:
        return extract_text_from_image(doc_path)
    elif file_ext == '.pdf':
        return extract_text_from_pdf(doc_path)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")
