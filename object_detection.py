from ultralytics import YOLO
import cv2

class ObjectDetection:
    def __init__(self, model_path='yolov8n.pt'):
        # Initialize YOLO model
        self.model = YOLO(model_path)

    def detect_objects(self, frame):
        # Perform detection on a single frame
        results = self.model(frame, verbose=False)
        annotated_frame = results[0].plot()  # Annotate detections
        return annotated_frame
