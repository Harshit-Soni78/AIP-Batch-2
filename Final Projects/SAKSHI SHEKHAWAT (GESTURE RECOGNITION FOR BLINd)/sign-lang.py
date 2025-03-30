import cv2
import mediapipe as mp
import pyttsx3
import math
import time

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 140)

# MediaPipe configurations
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
mp_drawing = mp.solutions.drawing_utils

# UI and gesture parameters
is_running = False
GESTURE_COOLDOWN = 1.5
last_gesture_time = 0
current_mode = "BLIND"  # Start with blind assistance mode
frame_width, frame_height = 640, 480  # Initial dimensions

# Color definitions
COLORS = {
    'open': (0, 255, 0),    # Green
    'closed': (0, 0, 255),  # Red
    'text': (255, 255, 255) # White
}

# Gesture definitions
BLIND_GESTURES = {
    "EMERGENCY": {'fingers': [0,0,0,0,0], 'message': "Emergency! Need immediate help!"},
    "REPEAT": {'fingers': [0,1,0,0,0], 'message': "Please repeat that"},
    "HELP": {'fingers': [0,1,1,0,0], 'message': "I need assistance"},
    "LOCATION": {'fingers': [1,0,0,0,1], 'message': "Where am I?"},
    "GUIDE": {'fingers': [1,1,0,0,0], 'message': "Please guide me"}
}

ASL_ALPHABET = {
    "A": {'fingers': [1,0,0,0,0], 'message': "A"},
    "B": {'fingers': [0,1,1,1,1], 'message': "B"},
    "C": {'fingers': [0,1,1,0,0], 'message': "C"},
    "D": {'fingers': [0,1,0,0,0], 'message': "D"},
    "E": {'fingers': [0,0,0,0,0], 'message': "E"},
    "F": {'fingers': [1,1,0,0,1], 'message': "F"},
    "G": {'fingers': [1,1,0,0,0], 'message': "G"},
    "H": {'fingers': [0,1,1,0,0], 'message': "H"},
    "I": {'fingers': [0,0,0,0,1], 'message': "I"},
    "K": {'fingers': [1,1,1,0,0], 'message': "K"},
    "L": {'fingers': [1,0,1,1,1], 'message': "L"},
    "M": {'fingers': [0,0,1,1,1], 'message': "M"},
    "N": {'fingers': [0,0,1,1,0], 'message': "N"},
    "O": {'fingers': [1,0,0,0,1], 'message': "O"},
    "P": {'fingers': [1,0,1,0,0], 'message': "P"},
    "Q": {'fingers': [1,0,0,1,0], 'message': "Q"},
    "R": {'fingers': [0,0,0,1,0], 'message': "R"},
    "S": {'fingers': [0,0,0,0,0], 'message': "S"},
    "T": {'fingers': [1,0,0,0,1], 'message': "T"},
    "U": {'fingers': [0,1,1,0,1], 'message': "U"},
    "V": {'fingers': [0,1,1,0,0], 'message': "V"},
    "W": {'fingers': [0,1,1,1,0], 'message': "W"},
    "X": {'fingers': [1,0,1,0,0], 'message': "X"},
    "Y": {'fingers': [1,0,0,1,1], 'message': "Y"},
}

def calculate_angle(a, b, c):
    """Calculate joint angle using math module"""
    ang = math.degrees(math.atan2(c.y - b.y, c.x - b.x) - math.atan2(a.y - b.y, a.x - b.x))
    return ang + 360 if ang < 0 else ang

def get_finger_state(landmarks, handedness):
    """Improved finger state detection"""
    states = [False] * 5  # [thumb, index, middle, ring, pinky]
    
    # Thumb detection
    thumb_angle = calculate_angle(
        landmarks[mp_hands.HandLandmark.WRIST],
        landmarks[mp_hands.HandLandmark.THUMB_MCP],
        landmarks[mp_hands.HandLandmark.THUMB_TIP]
    )
    states[0] = thumb_angle > 160 if handedness == "Right" else thumb_angle < 20
    
    # Finger detection
    for finger, idx in zip(
        [mp_hands.HandLandmark.INDEX_FINGER_PIP,
         mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
         mp_hands.HandLandmark.RING_FINGER_PIP,
         mp_hands.HandLandmark.PINKY_PIP],
        [1, 2, 3, 4]
    ):
        angle = calculate_angle(
            landmarks[finger - 2],
            landmarks[finger],
            landmarks[finger + 2]
        )
        states[idx] = angle < 80
    
    return states

def draw_landmarks(frame, hand_landmarks):
    """Draw hand points and connections without labels"""
    mp_drawing.draw_landmarks(
        frame,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=COLORS['open'], thickness=2),
        mp_drawing.DrawingSpec(color=COLORS['closed'], thickness=2)
    )

def detect_gesture(finger_states):
    """Detect gesture based on current mode"""
    if current_mode == "BLIND":
        for gesture, data in BLIND_GESTURES.items():
            if finger_states == data['fingers']:
                return gesture, data['message']
    else:
        for letter, data in ASL_ALPHABET.items():
            if finger_states == data['fingers']:
                return letter, data['message']
    return None, None

def draw_ui(frame):
    """Draw user interface elements"""
    global frame_width, frame_height
    frame_height, frame_width = frame.shape[:2]
    
    # Mode button (left)
    mode_color = COLORS['open'] if current_mode == "BLIND" else COLORS['closed']
    cv2.rectangle(frame, (10, 10), (160, 60), mode_color, -1)
    cv2.putText(frame, current_mode, (30, 45), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, COLORS['text'], 2)
    
    # Start/Stop button (right)
    button_color = COLORS['open'] if is_running else COLORS['closed']
    cv2.rectangle(frame, (frame_width-160, 10), (frame_width-10, 60), 
                 button_color, -1)
    cv2.putText(frame, "RUN" if is_running else "STOP", 
               (frame_width-140, 45), cv2.FONT_HERSHEY_SIMPLEX,
               0.8, COLORS['text'], 2)

def mouse_callback(event, x, y, flags, param):
    global is_running, current_mode, frame_width, frame_height
    if event == cv2.EVENT_LBUTTONDOWN:
        # Mode button (left: 10-160x, 10-60y)
        if 10 <= x <= 160 and 10 <= y <= 60:
            current_mode = "ASL" if current_mode == "BLIND" else "BLIND"
        
        # Start/Stop button (right)
        if (frame_width-160) <= x <= (frame_width-10) and 10 <= y <= 60:
            is_running = not is_running

# Main processing loop
cap = cv2.VideoCapture(0)
cv2.namedWindow('Gesture Assistant')
cv2.setMouseCallback('Gesture Assistant', mouse_callback)

try:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        draw_ui(frame)  # Update UI first to get proper dimensions

        if is_running:
            # Process hand gestures
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)
            
            current_gesture = None
            current_message = None

            if results.multi_hand_landmarks:
                for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    draw_landmarks(frame, hand_landmarks)
                    
                    # Get handedness and finger states
                    handedness = results.multi_handedness[hand_idx].classification[0].label
                    finger_states = get_finger_state(hand_landmarks.landmark, handedness)
                    
                    # Detect gesture
                    gesture, message = detect_gesture(finger_states)
                    if gesture and (time.time() - last_gesture_time) > GESTURE_COOLDOWN:
                        current_gesture = gesture
                        current_message = message
                        last_gesture_time = time.time()
                        engine.say(message)
                        engine.runAndWait()

            # Display recognition results
            if current_gesture:
                cv2.putText(frame, f"Detected: {current_gesture}", 
                            (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, COLORS['open'], 2)

        cv2.imshow('Gesture Assistant', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

except Exception as e:
    print(f"Error: {e}")
finally:
    cap.release()
    cv2.destroyAllWindows()
    engine.stop()