import cv2
import pytesseract
from autocorrect import Speller

def autocorrect_paragraph(text):
    spell = Speller(lang="en")  # English autocorrector
    return spell(text)

def extract_text_from_image(image_path):
    """Extracts text from an image using Tesseract OCR."""
    # Convert to grayscale (improves OCR accuracy)
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if len(image.shape) == 2:  # Already grayscale
        gray = image  
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale if needed
    
    # Apply thresholding (optional, improves results for some images)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Run OCR
    text = pytesseract.image_to_string(thresh)
    
    return autocorrect_paragraph(text) 
