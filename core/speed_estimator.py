import numpy


class SpeedEstimator:
    def __init__(self, pixels_per_meter=10, fps=30):
        self.previous_positions = {}
        self.pixels_per_meter = pixels_per_meter
        self.fps = fps

    def estimate(self, tracked_objects):
        speeds = {}
        for object_id, (cx, cy, box, class_id,confidence) in tracked_objects.items():
            if object_id in self.previous_positions:
                px, py = self.previous_positions[object_id]
                distance = numpy.hypot(cx - px, cy - py)

                meters = distance / self.pixels_per_meter

                time_second = 1 / self.fps

                speed_meter_per_second = meters / time_second
                speed_km_per_hour = speed_meter_per_second * 3.6

                speeds[object_id] = (round(speed_km_per_hour, 1))

            self.previous_positions[object_id] = (cx, cy)
        return speeds
