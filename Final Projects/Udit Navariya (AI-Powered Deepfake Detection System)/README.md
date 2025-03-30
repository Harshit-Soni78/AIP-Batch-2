# Deepfake Detection API

A FastAPI-based application that detects potential deepfakes in images and videos using computer vision techniques. This project analyzes various visual features to identify manipulated media content.

## Features

- Image and video analysis support
- Real-time deepfake detection
- Multiple detection metrics:
  - Edge density analysis
  - Color consistency checking
  - Texture complexity evaluation
- RESTful API interface
- Support for common image formats (PNG, JPG, JPEG) and videos (MP4)

## Prerequisites

- Python 3.10 or higher
- OpenCV
- FastAPI
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd finalkafinal
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:
```bash
python app.py
```

2. The server will start at `http://localhost:8000`

3. Access the API documentation:
   - Open your browser and navigate to `http://localhost:8000/docs`
   - This will show the interactive Swagger UI documentation

4. Using the API:
   - Click on the `/analyze` endpoint
   - Click "Try it out"
   - Upload an image or video file
   - Click "Execute"

## API Endpoints

### POST /analyze
Analyzes an uploaded image or video file for potential deepfake indicators.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (image or video file)

**Response:**
```json
{
    "is_deepfake": boolean,
    "confidence": float,
    "details": [
        {
            "score": float,
            "edge_density": float,
            "color_consistency": float,
            "texture_complexity": float
        }
    ]
}
```

## Detection Methodology

The deepfake detection is based on the analysis of several visual features:

1. **Edge Density**: Analyzes the distribution and complexity of edges in the image
2. **Color Consistency**: Checks for unnatural color patterns and inconsistencies
3. **Texture Complexity**: Evaluates the complexity of textures in the image

## Error Handling

The API returns appropriate error messages for:
- Unsupported file types
- Failed file uploads
- Processing errors
- No face detected in images

## Project Structure

```
finalkafinal/
├── app.py              # Main FastAPI application
├── deepfake_detector.py # Core detection logic
├── requirements.txt    # Project dependencies
├── uploads/           # Temporary upload directory
└── README.md          # Project documentation
```

## Contributing

Feel free to submit issues and enhancement requests!

## Acknowledgments

- OpenCV for computer vision capabilities
- FastAPI for the web framework
- Contributors and maintainers of all dependencies
