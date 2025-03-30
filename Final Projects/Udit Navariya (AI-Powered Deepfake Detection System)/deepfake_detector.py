import cv2
import numpy as np
from PIL import Image
import os
from pathlib import Path

class DeepfakeDetector:
    def __init__(self):
        # Initialize parameters for detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
    def analyze_image(self, image_path):
        """Analyze an image for potential deepfake indicators."""
        try:
            # Read image
            img = cv2.imread(image_path)
            if img is None:
                return {'error': 'Could not read image'}
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) == 0:
                return {'error': 'No face detected in the image'}
            
            # Analyze each face
            results = []
            for (x, y, w, h) in faces:
                face = img[y:y+h, x:x+w]
                
                # Calculate face metrics
                metrics = self._calculate_face_metrics(face)
                results.append(metrics)
            
            # Calculate overall score
            avg_score = np.mean([r['score'] for r in results])
            
            return {
                'is_deepfake': bool(avg_score > 0.7),
                'confidence': float(avg_score),
                'details': results
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def analyze_video(self, video_path):
        """Analyze a video for potential deepfake indicators."""
        try:
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                return {'error': 'Could not open video'}
            
            frame_results = []
            frame_count = 0
            max_frames = 30  # Limit analysis to first 30 frames
            
            while cap.isOpened() and frame_count < max_frames:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Save frame temporarily
                temp_path = f'temp_frame_{frame_count}.jpg'
                cv2.imwrite(temp_path, frame)
                
                # Analyze frame
                result = self.analyze_image(temp_path)
                if 'error' not in result:
                    frame_results.append(result)
                
                # Clean up
                os.remove(temp_path)
                frame_count += 1
            
            cap.release()
            
            if not frame_results:
                return {'error': 'No valid frames analyzed'}
            
            # Calculate overall video score
            avg_score = np.mean([r['confidence'] for r in frame_results])
            
            return {
                'is_deepfake': bool(avg_score > 0.7),
                'confidence': float(avg_score),
                'frames_analyzed': frame_count
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def _calculate_face_metrics(self, face):
        """Calculate various metrics for face analysis."""
        # Convert to grayscale
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        
        # Calculate edge density
        edges = cv2.Canny(gray, 100, 200)
        edge_density = np.sum(edges > 0) / edges.size
        
        # Calculate color consistency
        hsv = cv2.cvtColor(face, cv2.COLOR_BGR2HSV)
        color_std = np.std(hsv[:,:,1])  # Saturation channel
        
        # Calculate texture complexity
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        texture_complexity = np.std(laplacian)
        
        # Combine metrics into a score
        score = (edge_density * 0.4 + 
                (1 - color_std/255) * 0.3 + 
                (1 - texture_complexity/1000) * 0.3)
        
        return {
            'score': float(score),
            'edge_density': float(edge_density),
            'color_consistency': float(1 - color_std/255),
            'texture_complexity': float(1 - texture_complexity/1000)
        }

def main():
    # Initialize detector
    detector = DeepfakeDetector()
    
    # Get file path from user
    file_path = input("Enter the path to your image or video file: ")
    
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return
    
    # Get file extension
    file_ext = Path(file_path).suffix.lower()
    
    # Analyze file based on type
    if file_ext in ['.png', '.jpg', '.jpeg']:
        result = detector.analyze_image(file_path)
    elif file_ext == '.mp4':
        result = detector.analyze_video(file_path)
    else:
        print("Error: Unsupported file type. Please use .png, .jpg, .jpeg, or .mp4 files.")
        return
    
    # Display results
    if 'error' in result:
        print(f"Error: {result['error']}")
        return
    
    print("\nAnalysis Results:")
    print("-" * 20)
    print(f"Result: {'Deepfake Detected' if result['is_deepfake'] else 'Authentic'}")
    print(f"Confidence: {result['confidence']*100:.2f}%")
    
    if 'details' in result:
        print("\nDetailed Analysis:")
        for i, detail in enumerate(result['details'], 1):
            print(f"\nFace {i}:")
            print(f"Score: {detail['score']*100:.2f}%")
            print(f"Edge Density: {detail['edge_density']*100:.2f}%")
            print(f"Color Consistency: {detail['color_consistency']*100:.2f}%")
            print(f"Texture Complexity: {detail['texture_complexity']*100:.2f}%")

if __name__ == "__main__":
    main()