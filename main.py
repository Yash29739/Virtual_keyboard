import cv2
import mediapipe as mp
import pygame
import time

# Initialize Pygame mixer
pygame.mixer.init()

# Load sounds
sounds = {
    'A': pygame.mixer.Sound('assets/a_note(c6).mp3'),
    'B': pygame.mixer.Sound('assets/b_note(a6).mp3'),
    'C': pygame.mixer.Sound('assets/c_note(f6).mp3'),
    'D': pygame.mixer.Sound('assets/d_note(g6).mp3'),
    'E': pygame.mixer.Sound('assets/e_note(b6).mp3'),
    'F': pygame.mixer.Sound('assets/f_note(e6).mp3'),
    'G': pygame.mixer.Sound('assets/g_note(piano).mp3'),
    'H': pygame.mixer.Sound('assets/h_note(do).mp3'),
    'I': pygame.mixer.Sound('assets/i_note(fa).mp3'),
    'J': pygame.mixer.Sound('assets/j_note(si).mp3'),
}

# Setup camera
cap = cv2.VideoCapture(0)
width, height = 1600, 1000
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Key layout
keys = list(sounds.keys())
key_width, key_height = 100, 200
spacing = 20
margin_x = 50
margin_y = height - key_height - 50

# Cooldown tracking
last_pressed = {}
cooldown = 0.4  # seconds

# Fingertips
fingertip_ids = [
    mp_hands.HandLandmark.THUMB_TIP,
    mp_hands.HandLandmark.INDEX_FINGER_TIP,
    mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
    mp_hands.HandLandmark.RING_FINGER_TIP,
    mp_hands.HandLandmark.PINKY_TIP,
]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (width, height))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    overlay = frame.copy()
    key_positions = []

    # Draw transparent keys
    for i, key in enumerate(keys):
        x1 = margin_x + i * (key_width + spacing)
        y1 = margin_y
        x2, y2 = x1 + key_width, y1 + key_height
        key_positions.append((key, x1, y1, x2, y2))

        # Transparent white key
        cv2.rectangle(overlay, (x1, y1), (x2, y2), (255, 255, 255), -1)
        alpha = 0.4
        cv2.addWeighted(overlay[y1:y2, x1:x2], alpha, frame[y1:y2, x1:x2], 1 - alpha, 0, frame[y1:y2, x1:x2])

        # Border and text
        cv2.rectangle(frame, (x1, y1), (x2, y2), (200, 200, 200), 2)
        cv2.putText(frame, key, (x1 + 25, y1 + 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (50, 50, 50), 3)

    # Finger tip detection and key interaction
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for tip_id in fingertip_ids:
                lm = hand_landmarks.landmark[tip_id]
                x, y = int(lm.x * width), int(lm.y * height)
                cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

                for key, x1, y1, x2, y2 in key_positions:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        now = time.time()
                        if key not in last_pressed or now - last_pressed[key] > cooldown:
                            sounds[key].play()
                            last_pressed[key] = now
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                        break

    cv2.imshow("Virtual Air Keyboard", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
