from ultralytics import YOLO

model = YOLO("best.pt")

def detect_person(frame):
    results = model(frame, conf=0.5, imgsz=416)

    person_detected = False
    for result in results:
        for cls in result.boxes.cls:
            if int(cls) == 0:
                person_detected = True

    return person_detected, results
