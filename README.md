# Car Detection, Tracking & Speed Estimation with YOLOv8

Real-time object detection, tracking, and speed estimation for cars, trucks, and buses using **YOLOv8** and **OpenCV** in Python.

---

## 📉 Features

* ✅ Real-time vehicle detection using YOLOv8
* ✅ Centroid-based custom object tracker (lightweight, no external tracking libs)
* ✅ Speed estimation in km/h based on pixel displacement and frame rate
* ✅ Configurable detection classes: car, bus, truck
* ✅ Clean and modular architecture for extensibility

---

## 🧬 How it works

1. Video is read frame-by-frame
2. Vehicles are detected using the YOLOv8 model
3. The center (cx, cy) of each object is calculated
4. Tracker matches detected objects to previously seen ones based on distance
5. Speed is estimated using:

```text
speed = (pixel_distance / pixels_per_meter) / time_per_frame (converted to km/h)
```

---

## 🧰 Technologies Used

| Tool        | Purpose                               |
| ----------- | ------------------------------------- |
| Python 3.13 | Main programming language             |
| OpenCV      | Frame reading, drawing, preprocessing |
| YOLOv8      | Vehicle detection                     |
| NumPy       | Distance calculation                  |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/vehicle-speed-tracker.git
cd vehicle-speed-tracker
```

### 2. Create and activate virtual environment (optional)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## 📆 Configuration

Edit the `config.py` file:

```python
VIDEO_PATH = "videos/traffic.mp4"
CONFIDENCE_THRESHOLD = 0.5
PIXELS_PER_METER = 10
FPS = 30
```

You can also change `target_classes` in `main.py`:

```python
target_classes = {2, 5, 7}  # car, bus, truck
```

---

## 📁 Project Structure

```
vehicle-speed-tracker/
├── core/
│   ├── object_detector.py
│   ├── object_tracker.py
│   ├── speed_estimator.py
│   └── video_reader.py
├── utils/
│   └── drawing.py
├── config.py
├── main.py
├── README.md
└── requirements.txt
```

---

## 📊 Sample Output

The app displays a live window with bounding boxes and speed:

```
Car ID: 4 | Speed: 52.3 km/h
Truck ID: 1 | Speed: 88.7 km/h
```

* Red boxes indicate vehicles exceeding speed threshold (e.g., 100 km/h)
* Class name and speed are drawn above the bounding box

---

## 🚫 Future Improvements

* [ ] Save results to CSV or database
* [ ] Web dashboard with Flask or Streamlit
* [ ] Real-time camera support
* [ ] Entry/exit zone logic
* [ ] Vehicle counting & heatmaps

---

## 🙌 Author

Created with ❤️ by **Armin Yaghoubi**

> If you liked this project, consider starring the repo and following for more!

---

## 📄 License

MIT License — free for personal and commercial use.
