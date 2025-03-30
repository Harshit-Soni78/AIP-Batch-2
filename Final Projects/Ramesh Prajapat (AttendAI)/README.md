# AttendAI - Face Recognition Based Attendance System

## Problem Statement

Traditional attendance systems are time-consuming, prone to proxy attendance, and require manual record maintenance. Educational institutions and organizations need an automated, secure, and efficient attendance tracking solution that eliminates these issues while providing reliable attendance records.

## Description

AttendAI is an intelligent attendance tracking system that uses facial recognition technology to automate the attendance recording process. Built with Python, Tkinter, and OpenCV, this application captures student/employee images, trains a recognition model, and marks attendance by identifying registered individuals through a webcam. AttendAI eliminates manual attendance-taking, prevents proxy attendance, and maintains digital attendance records with timestamps.

## Features

- **Face Recognition**: Automatically identifies registered individuals using facial recognition
- **User Registration**: Simple interface to register new users with ID and name
- **Real-time Attendance**: Marks attendance with date and time stamps
- **Secure Admin Panel**: Password-protected admin functions
- **Attendance Reports**: Generate and download attendance reports
- **User-friendly Interface**: Clean and intuitive GUI built with Tkinter
- **Attendance Verification**: Stores captured images as proof of attendance
- **Data Management**: Maintains student details and attendance records in CSV format

## Prerequisites

To run AttendAI, you need the following:

1. **Python 3.7+**
2. **Required Python packages**:
   - OpenCV (cv2)
   - NumPy
   - Pandas
   - Pillow (PIL)
   - Tkinter (usually comes with Python)
   - Jupyter Notebook (if running the `.ipynb` version)
3. **Webcam** - Built-in or external webcam is required for image capture and recognition

## Installation Guide

### Step 1: Install Python

1. Download Python 3.7+ from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Verify installation by running `python --version` in command prompt or terminal

### Step 2: Install Required Packages

Run the following command in your terminal or command prompt:

```bash
pip install jupyter opencv-python numpy pandas pillow
```

**Note:**

- `tkinter` comes pre-installed with Python. If you face issues, install it using:
  ```bash
  pip install tk
  ```
- `csv`, `datetime`, `os`, and `time` are built-in Python modules, so no installation is needed.

### Step 3: Clone the Repository

```bash
git clone https://github.com/PRAJAPATBOI/AttendAI.git
cd AttendAI
```

### Step 4: Run the Project

You can run the project in **two ways**:

1. **Using Jupyter Notebook**:

   - Open Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open `attendance_app.ipynb`
   - Execute the cells step by step

2. **Using a Python Script**:

   - Copy the code from `attendance_app.ipynb`
   - Paste it into a new file named `app.py`
   - Run the script:
     ```bash
     python app.py
     ```

## Usage Guide

### Registering a New User

1. Enter the ID and Name in the right panel
2. Click "Take Images" to capture face data (100 samples will be taken)
3. Click "Save Profile" to save user data and train the recognition model

### Taking Attendance

1. Click "Take Attendance" in the left panel
2. The system will open the webcam and identify registered users
3. Upon successful recognition, attendance is marked with a timestamp

### Generating Reports

1. Go to Admin Panel → Generate Report
2. Enter the admin password
3. Select report type (All Students or Particular Student)
4. View and download the report as needed

## Project Structure

- `TrainingImage/`: Stores captured user images
- `TrainingImageLabel/`: Contains trained model data
- `StudentDetails/`: Stores user information
- `Attendance/`: Daily attendance records
- `Reports/`: Generated attendance reports
- `Attendance_Images/`: Proof of attendance images

## Initial Setup

- The default admin password needs to be set during the first run
- Create required directories if they don't exist automatically

## Note

Ensure good lighting conditions for better face recognition accuracy.

