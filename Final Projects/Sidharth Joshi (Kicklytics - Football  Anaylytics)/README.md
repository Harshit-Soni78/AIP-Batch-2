# Kicklytics Project - Football + Analytics

## Overview

This project analyzes football match videos to track players, assign teams, determines ball possession and referees. It uses YOLO-based object detection, tracking algorithms, and custom logic for team and ball assignment. It is based on deep learning and image recognition.

![Screenshot 2025-03-29 235122](https://github.com/user-attachments/assets/20e58aa2-3adc-4607-858a-9d74453d3f03)

## Features
- **Player and Ball Tracking**: Detects and tracks players and the ball across video frames.
- **Team Assignment**: Assigns players to teams based on their positions and colors.
- **Ball Possession**: Identifies which player has possession of the ball.
- **Video Annotation**: Generates an output video with annotations for tracks, teams, and ball possession.

## How It Works
- Video Reading: The input video is read frame by frame using OpenCV.
- Object Detection and Tracking: YOLO-based model detects players and the ball, and tracks their positions.
- Team Assignment: Players are assigned to teams based on their colors.
- Ball Possession: The ball is assigned to the nearest player.
- Video Annotation: Tracks, team colors, and ball possession are drawn on the video frames.

## Files and Directories
- main.py: Main script to run the project.
- player_ball_assigner/: Logic for assigning the ball to players.
- team_assigner/: Logic for assigning players to teams.
- trackers/: YOLO-based object detection and tracking.
- input_videos/: Directory for input videos.
- output_videos/: Directory for output videos.
- model/: Pre-trained YOLO models.

  
## Trained Model
- [Trained Yolo v5lu model](https://drive.google.com/file/d/1A4xofTlNuG2hxRY38u8rTKSMJIaVLCFL/view?usp=sharing)
- [Roboflow dataset](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1)

## Sample input video
-  [Sample input video](https://drive.google.com/file/d/1LtXotImyfxwHYCu1vxPHkxL2SA2_FmPE/view?usp=sharing)

## Output video


https://github.com/user-attachments/assets/fcb2c017-c33b-402c-a9af-57aad93aba1f


## Requirements
To run this project, you need to have the following requirements installed:
- Python==3.12.0
- Ultralytics>=8.3.97
- Supervision==0.25.1
- OpenCv-Python==4.11.0.86
- NumPy==1.26.4
- MatPlotlib==3.9.1
- Pandas==2.2.2
- Roboflow==1.1.58
- SciPy==1.14.0


## 🚀 **Getting Started**

### ✅ **1. Clone the Repository**
- First, clone the project repository to your local machine.
- git clone https://github.com/sidharth031/Kicklytics31.git
- cd Kicklytics31
  
### ✅ **2. Install Required Libraries**
pip install -r requirements.txt

### ✅ *3. Download YOLO Model*
[Link to download](https://docs.ultralytics.com/models/yolo11/)

### ✅ *4. Setup The Dataset*
[Roboflow dataset , get your unique api key too](https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1)

### ✅ *5. Start training with this dataset*
To get a model which i got as best.pt, which i dont train again and again as i have saved this model in pickle file.

### ✅ *6. Start Running the project*
1. Detect Players and the Ball
2. Configure Model Parameters
3. Train the AI Model
4. Evaluate the AI Model
5. Implement Object Tracking
6. Color assignement for different team according to k means clustering
7. Ball Interpolation
8. Player Assign as per possesion of ball

### ✅ *7. Finally run main project*
  - Place your input video in the input_videos/ directory.
  - Run the main script: python main.py
  - The output video with annotations will be saved in the output_videos/ directory.




## Future Improvements
- Enhance team assignment logic for better accuracy.
- Improve ball possession detection using advanced algorithms.
- Add support for real-time video processing.
- Tracking speed and distance of players.
- Useful in VAR technology.
- Player pass count
- Team ball control

## Contact
For any questions or feedback, please contact Sidharth Joshi at [Gmail](sidharthjoshi74@gmail.com) and [Linkedin](www.linkedin.com/in/sidharth-joshi-7b01a5205).








