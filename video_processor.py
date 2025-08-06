import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = fps * 2  # every 2 seconds
    events = []

    frame_id = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % frame_interval == 0:
            results = model.predict(frame)
            for result in results:
                for box in result.boxes:
                    cls = model.names[int(box.cls[0])]
                    conf = float(box.conf[0])
                    if conf > 0.5:
                        timestamp = frame_id // fps
                        events.append(f"At {timestamp}s: Detected {cls}")
        frame_id += 1

    cap.release()
    return events
