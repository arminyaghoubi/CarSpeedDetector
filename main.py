import cv2
from config import VIDEO_PATH
from utils.drawing import draw_boxes
from core.video_reader import VideoReader
from core.object_tracker import ObjectTracker
from core.object_detector import ObjectDetector
from core.speed_estimator import SpeedEstimator


def main():
    tracker = ObjectTracker()
    speed_estimator = SpeedEstimator()
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
                class_id = int(box.cls[0])
                if class_id not in target_classes:
                    continue
                confidence = float(box.conf[0])
                x1, y1, x2, y2 = box.xyxy[0]
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                centers.append((cx, cy, box, class_id, confidence))

        tracked_objects = tracker.update(centers)
        speeds = speed_estimator.estimate(tracked_objects)

        final_result = []
        for object_id, (cx, cy, box, class_id, confidence) in tracked_objects.items():
            final_result.append({
                'object_id': object_id,
                'class_id': class_id,
                'confidence': confidence,
                'box': box,
                'speed': speeds.get(object_id)
            })

        draw_boxes(frame, final_result, class_names, target_classes)

        cv2.imshow("Traffic Video", frame)

        if cv2.waitKey(30) & 0XFF == ord('q'):
            break

    reader.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
