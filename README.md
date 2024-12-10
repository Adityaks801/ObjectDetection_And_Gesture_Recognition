Object Detection and Gesture Recognition
This project implements real-time Object Detection using YOLOv5 and Gesture Recognition using MediaPipe Hands, powered by OpenCV. The application processes video feeds from a webcam to detect objects and recognize gestures, providing an interactive way to toggle between the two modes.

Features
Real-time Object Detection using YOLOv5.
Real-time Gesture Recognition using MediaPipe Hands.
Modular design for easy integration and extension.
Toggle between object detection and gesture recognition.



Press O to switch to Object Detection.
Press G to switch to Gesture Recognition.
Press Q to quit the application.


   
object-gesture-project/
│
├── main.py                # Entry point for the application
├── object_detection.py    # Logic for object detection
├── gesture_recognition.py # Logic for gesture recognition
├── models/                # Pretrained YOLOv5 models (if required)
├── utils/                 # Helper functions (optional)
├── data/                  # Gesture datasets (optional)
└── README.md              # Documentation



Technologies Used

Python
OpenCV for video processing
YOLOv5 for object detection
MediaPipe Hands for gesture recognition
Torch for loading pretrained models
