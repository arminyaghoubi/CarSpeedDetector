import numpy


class ObjectTracker:
    def __init__(self, distance_threshold=30):
        self.next_id = 0
        self.objects = {}
        self.distance_threshold = distance_threshold

    def update(self, detections):
        updated_objects = {}
        ids = set()

        for cx, cy, box, class_id, confidence in detections:
            matched_id = None
            min_distance = float("inf")

            for object_id, (px, py, b, clsid, conf) in self.objects.items():
                distance = numpy.hypot(cx - px, cy - py)
                if distance < self.distance_threshold and object_id not in ids and distance < min_distance:
                    matched_id = object_id
                    min_distance = distance

            if matched_id is not None:
                updated_objects[matched_id] = (cx, cy, box, class_id, confidence)
                ids.add(matched_id)
            else:
                updated_objects[self.next_id] = (cx, cy, box, class_id, confidence)
                self.next_id += 1

        self.objects = updated_objects
        return self.objects
