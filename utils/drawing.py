import cv2


def draw_boxes(frame, results,class_names,target_classes):
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            if class_id in target_classes:
                confidence = float(box.conf[0])
                if confidence < 0.5:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                label = f"{class_names[class_id]}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
