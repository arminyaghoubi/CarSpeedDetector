import cv2


def draw_boxes(frame, results, class_names, target_classes):
    for result in results:
        for box in result["box"]:
            class_id = result["class_id"]
            if class_id in target_classes:
                confidence = result["confidence"]
                if confidence < 0.5:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                if result['speed']:
                    label = f"{class_names[class_id]}({result['speed']} Km/h)"
                    rectangle_color = (0, 0, 255) if result['speed'] > 100 else (0, 255, 0)
                else:
                    label = f"{class_names[class_id]}"
                    rectangle_color=(0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), rectangle_color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 1, rectangle_color, 2)
