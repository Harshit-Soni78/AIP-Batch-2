# Smooth Face Tracking with Hand Gesture Controls & Writing Pad

## Overview
This project utilizes OpenCV and MediaPipe to implement a real-time face tracking system with smooth motion, hand gesture-based zooming, and a virtual writing pad. The system detects faces, tracks movement smoothly using exponential smoothing, and enables zoom control based on hand gestures. Additionally, users can toggle a virtual writing pad to draw using hand tracking, with an optional eraser mode.

## Features
- **Smooth Face Tracking:** Uses exponential smoothing for stable face tracking.
- **Hand Gesture-Based Zooming:** Adjust zoom level dynamically using thumb and finger distance.
- **Virtual Writing Pad:** Draw on the screen using hand gestures, with an optional eraser mode.
- **Real-Time Webcam Processing:** Works with live video feed.
- **Adjustable Viewport and Zoom:** Automatically adapts based on detected face size.

## Dependencies
Ensure you have the following dependencies installed before running the script:

```bash
pip install opencv-python mediapipe numpy
```

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Yuvraj657/Face-Tracker-WebCam-with-Gesture-Controls.git
   cd Face-Tracker-WebCam-with-Gesture-Controls
   ```
2. Run the script:
   ```bash
   python model.py
   ```

## Controls
- **`q`** - Quit the program
- **`t`** - Toggle the writing pad
- **`e`** - Toggle eraser mode
- **`+`** - Increase eraser size
- **`-`** - Decrease eraser size

## How It Works
- The webcam captures video and processes frames using OpenCV.
- MediaPipe detects faces and hands in the frame.
- Face tracking applies exponential smoothing to avoid jitter.
- Hand gestures determine zoom level dynamically.
- The writing pad feature allows drawing using finger movement.

## Future Enhancements
- Implement gesture-based toggling for writing pad and eraser.
- Improve zooming responsiveness for smoother experience.
- Add multi-face tracking support.



## Author
Yuvraj Singh(A.I. and Data Science)

