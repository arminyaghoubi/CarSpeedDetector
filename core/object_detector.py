from ultralytics import YOLO


class ObjectDetector:
    def __init__(self, model="yolov8n.pt"):
        self.model = YOLO(model)

    def detect(self, frame):
        results=self.model(frame,verbose=False)
        return results
