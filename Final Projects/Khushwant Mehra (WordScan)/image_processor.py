import cv2
import numpy as np
import matplotlib.pyplot as plt

def align_document(image_path):
    # Load image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur and edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    # Find the document shape (largest quadrilateral)
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        if len(approx) == 4:  # If 4 points are detected, we assume it's the document
            doc_corners = approx
            break

    # Get a top-down view of the document
    pts = doc_corners.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")

    # Order points: top-left, top-right, bottom-right, bottom-left
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # Define the new width and height
    (tl, tr, br, bl) = rect
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))

    # Perspective transform matrix
    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    aligned = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return aligned

def image_cleaner(image_path, processed_image_path):
    gray = cv2.cvtColor(align_document(image_path), cv2.COLOR_BGR2GRAY)
    
    # Perform adaptive thresholding
    img_thresh_adp = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)
    
    cv2.imwrite(processed_image_path, img_thresh_adp)
