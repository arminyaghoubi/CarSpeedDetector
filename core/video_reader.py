import cv2


class VideoReader:
    def __init__(self, path):
        self.capture = cv2.VideoCapture(path)
        if not self.capture.isOpened():
            raise IOError(f"Cannot open video file: {path}")

    def read_frame(self):
        ret, frame = self.capture.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.capture.release()
