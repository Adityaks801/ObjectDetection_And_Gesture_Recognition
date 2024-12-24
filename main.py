import cv2
from object_detection import ObjectDetection
from gesture_recognition import GestureRecognition

# Initialize object detection and gesture recognition classes
object_detector = ObjectDetection()
gesture_recognizer = GestureRecognition()

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Object Detection
    frame = object_detector.detect_objects(frame)

    # Step 2: Gesture Recognition
    frame = gesture_recognizer.recognize_gestures(frame)

    # Display the output
    cv2.imshow("Object Detection & Gesture Recognition", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
