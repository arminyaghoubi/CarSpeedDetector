import cv2
from config import VIDEO_PATH
from utils.drawing import draw_boxes
from core.object_tracker import ObjectTracker
from core.video_reader import VideoReader
from core.object_detector import ObjectDetector


def main():
    tracker = ObjectTracker()
    target_classes = {2, 5, 7}  # car, bus, truck
    detector = ObjectDetector()
    class_names = detector.model.names
    reader = VideoReader(VIDEO_PATH)

    while True:
        frame = reader.read_frame()
        if frame is None:
            break

        results = detector.detect(frame)

        centers = []
        for result in results:
            for box in result.boxes:
                if int(box.cls[0]) not in target_classes:
                    continue
                x1, y1, x2, y2 = box.xyxy[0]
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                centers.append((cx, cy))

        tracked_objects = tracker.update(centers)

        draw_boxes(frame, results, class_names, target_classes)

        cv2.imshow("Traffic Video", frame)

        if cv2.waitKey(30) & 0XFF == ord('q'):
            break

    reader.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
