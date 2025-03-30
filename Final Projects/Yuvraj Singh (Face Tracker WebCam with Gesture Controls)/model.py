import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Face Detection and Hand Detection
mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
face_detector = mp_face_detection.FaceDetection(min_detection_confidence=0.7)
hand_detector = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define initial viewport size (adjustable)
viewport_width = frame_width
viewport_height = frame_height

# Initialize face center tracking
center_x, center_y = frame_width // 2, frame_height // 2
alpha = 0.2  # Exponential smoothing factor (higher = smoother, but slower response)
zoom_factor = 1.0  # Default zoom level
zoom_speed = 0.03  # Adjusted speed for smoother zoom changes
zoom_step = 0.05  # Step size for zooming in and out

# Create a blank canvas for drawing
canvas = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
drawing = False  # Flag to track writing pad state
prev_x, prev_y = None, None

# Button to toggle writing pad
writing_pad_active = False
eraser_mode = False  # Toggle for eraser mode
eraser_size = 10  # Initial eraser size

def toggle_writing_pad():
    global writing_pad_active
    writing_pad_active = not writing_pad_active

def toggle_eraser():
    global eraser_mode
    eraser_mode = not eraser_mode

def increase_eraser_size():
    global eraser_size
    eraser_size = min(eraser_size + 10, 50)  # Max eraser size

def decrease_eraser_size():
    global eraser_size
    eraser_size = max(eraser_size - 10, 10)  # Min eraser size

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Mirror the video
    frame = cv2.flip(frame, 1)

    h, w = frame.shape[:2]
    
    # Convert frame to RGB (MediaPipe requires RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect faces
    face_results = face_detector.process(rgb_frame)
    
    # Detect hands
    hand_results = hand_detector.process(rgb_frame)
    
    if face_results.detections:
        # Get first detected face (highest confidence)
        face = face_results.detections[0]
        bboxC = face.location_data.relative_bounding_box

        # Convert bounding box to pixel coordinates
        x1, y1, w_box, h_box = (
            int(bboxC.xmin * w),
            int(bboxC.ymin * h),
            int(bboxC.width * w),
            int(bboxC.height * h),
        )

        # Compute face center
        face_center_x = x1 + w_box // 2
        face_center_y = y1 + h_box // 2

        # Apply exponential smoothing for smoother movement
        center_x = int(alpha * face_center_x + (1 - alpha) * center_x)
        center_y = int(alpha * face_center_y + (1 - alpha) * center_y)

        # Adjust zoom based on face size
        face_size = max(w_box, h_box)
        target_zoom = min(max(1.0, 1.8 - (face_size / w)), 2.0)
        zoom_factor += zoom_speed * (target_zoom - zoom_factor)

    # Check for hand gestures and drawing
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            index_x, index_y = int(index_tip.x * frame_width), int(index_tip.y * frame_height)
            thumb_x, thumb_y = int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)
            middle_x, middle_y = int(middle_tip.x * frame_width), int(middle_tip.y * frame_height)
            
            distance_thumb_index = np.linalg.norm(np.array([thumb_x, thumb_y]) - np.array([index_x, index_y]))
            distance_thumb_middle = np.linalg.norm(np.array([thumb_x, thumb_y]) - np.array([middle_x, middle_y]))
            
            # Zoom in/out based on thumb position relative to fingers
            if distance_thumb_index > 50 and distance_thumb_middle > 50:
                if thumb_y < index_y and thumb_y < middle_y:
                    zoom_factor = min(zoom_factor + zoom_step, 2.0)  # Zoom in
                elif thumb_y > index_y and thumb_y > middle_y:
                    zoom_factor = max(zoom_factor - zoom_step, 1.0)  # Zoom out

            if writing_pad_active:
                if eraser_mode:
                    cv2.circle(canvas, (index_x, index_y), eraser_size, (0, 0, 0), -1)  # Adjustable erase radius
                else:
                    if prev_x is not None and prev_y is not None:
                        cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), (255, 0, 0), 5)
                    prev_x, prev_y = index_x, index_y
    else:
        prev_x, prev_y = None, None  # Reset if no hands detected

    # Compute new viewport size based on zoom factor
    viewport_width = int(frame_width / zoom_factor)
    viewport_height = int(frame_height / zoom_factor)
    
    # Compute new viewport position
    x1 = max(0, min(center_x - viewport_width // 2, frame_width - viewport_width))
    y1 = max(0, min(center_y - viewport_height // 2, frame_height - viewport_height))
    x2, y2 = x1 + viewport_width, y1 + viewport_height
    
    # Crop and resize to match original frame size
    frame_cropped = frame[y1:y2, x1:x2]
    frame_resized = cv2.resize(frame_cropped, (frame_width, frame_height))
    
    # Overlay the drawing on the frame
    output_frame = cv2.addWeighted(frame_resized, 0.8, canvas, 0.5, 0)

    # Display a button on the frame
    cv2.rectangle(output_frame, (10, 10), (150, 50), (0, 255, 0), -1)
    cv2.putText(output_frame, "Toggle Pad", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
    cv2.imshow('Smooth Face Tracking with Hand Gesture Zoom & Writing Pad', output_frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('t'):
        toggle_writing_pad()
    elif key == ord('e'):
        toggle_eraser()
    elif key == ord('+'):
        increase_eraser_size()
    elif key == ord('-'):
        decrease_eraser_size()

cap.release()
cv2.destroyAllWindows()

