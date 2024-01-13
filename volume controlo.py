import cv2
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Set up audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Open the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to get hand landmarks
    results = hands.process(rgb_frame)

    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmarks for thumb and index finger
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Get the coordinates of thumb and index finger
            thumb_x, thumb_y = int(thumb.x * frame.shape[1]), int(thumb.y * frame.shape[0])
            index_x, index_y = int(index_finger.x * frame.shape[1]), int(index_finger.y * frame.shape[0])

            # Calculate the distance between thumb and index finger
            distance = calculate_distance(thumb_x, thumb_y, index_x, index_y)

            # Map the distance to a volume range (adjust as needed)
            volume_level = max(0.0, min(distance / 300.0, 1.0))

            # Set the volume based on the calculated level
            volume.SetMasterVolumeLevelScalar(volume_level, None)

            # Draw a line between thumb and index finger
            cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (0, 255, 0), 3)

    # Display the frame
    cv2.imshow('Gesture Volume Control', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
