# Gesture Recognition for Blind Assistance 👋🔊

## Overview 🌐
This project implements a real-time gesture recognition system designed to assist visually impaired individuals by converting hand gestures into audible speech. The system uses computer vision and machine learning to detect hand gestures with two operational modes:
1. **👁️🗨️ Blind Assistance Mode**: Predefined gestures for common assistance requests
2. **🤟 ASL Mode**: American Sign Language alphabet recognition

## ✨ Key Features
- 🖐️ Real-time hand gesture detection using MediaPipe
- 🔊 Text-to-speech feedback for recognized gestures
- 🎨 Simple UI with toggle buttons for mode switching
- ⏳ Cooldown period to prevent gesture spamming
- 👀 Visual feedback of recognized gestures
- 💡 Future-ready for wearable integration

## 🎯 Target Audience
This system is designed for:
- 👩🦯 Visually impaired individuals
- 🤟 ASL users
- 🏥 Healthcare and accessibility applications

## 📋 Requirements
- Python 3.6+ 🐍
- OpenCV (`pip install opencv-python`) 📷
- MediaPipe (`pip install mediapipe`) ✋
- pyttsx3 (`pip install pyttsx3`) 🔊

## 🤲 Gesture Definitions

### 👁️🗨️ Blind Assistance Mode Gestures
| Gesture   | Finger State | Message                      | Emoji |
|-----------|--------------|------------------------------|-------|
| EMERGENCY | [0,0,0,0,0]  | "Emergency! Need help!"       | 🆘    |
| REPEAT    | [0,1,0,0,0]  | "Please repeat that"          | 🔁    |
| HELP      | [0,1,1,0,0]  | "I need assistance"           | 🙋    |
| LOCATION  | [1,0,0,0,1]  | "Where am I?"                | 🗺️    |
| GUIDE     | [1,1,0,0,0]  | "Please guide me"            | 🚶‍♂️   |

### 🤟 ASL Mode
Recognizes letters A-Z (excluding J) from American Sign Language alphabet with visual feedback 👆👇🖐️

## 🚀 Usage Guide
1. Run the script: `python gesture_assistant.py` 💻
2. The system will open a camera window with:
   - 🔘 Left button: Toggle between Blind/ASL modes
   - 🔘 Right button: Start/Stop recognition
3. Make gestures to trigger voice feedback 🗣️

## ⚙️ Technical Details
- Uses MediaPipe's hand landmark model ✋
- Calculates joint angles for precise detection 📐
- 1.5s cooldown between detections ⏱️
- Visual feedback overlay 👀

## 🔮 Future Roadmap
- **Wearable Integration** ⌚
  - Smart wristbands for hands-free interaction
  - Haptic feedback for tactile response 📳
  - IoT connectivity for remote monitoring 🌐
  
- **Enhanced Features** 🚀
  - Multilingual speech synthesis 🌍
  - Deep learning gesture recognition 🧠
  - Mobile app companion 📱
  - Gesture sequences for complex commands 🔢

- **Accessibility Improvements** ♿
  - Voice command integration 🎤
  - Environmental awareness features 🏙️
  - Emergency alert system 🚨

## 📜 License
MIT License - Open Source ✅

## 🙏 Acknowledgments
- MediaPipe for hand tracking ✋
- pyttsx3 for TTS 🔊
- OpenCV for vision capabilities 👁️
- All contributors and testers 🤝

---

💡 **Prototype Note**: Current version focuses on camera-based recognition, with wearable integration planned for Phase 2 development. We welcome collaborators to help make this technology more accessible! 🌈
