import cv2
import time
from ultralytics import YOLO

# Load model
model = YOLO("model/best.pt")

# Camera
cap = cv2.VideoCapture(0)

# Delay settings
last_detect_time = 0
cooldown = 5  # seconds

# Appliance states
appliance1 = False
appliance2 = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detected = False

    for r in results:
        for box in r.boxes:
            detected = True

    current_time = time.time()

    if detected and (current_time - last_detect_time > cooldown):
        print("Person detected!")

        # CONTROL APPLIANCES HERE
        appliance1 = True
        appliance2 = True

        print("Appliance 1 ON")
        print("Appliance 2 ON")

        last_detect_time = current_time

    if not detected:
        appliance1 = False
        appliance2 = False

    # Show frame
    annotated = results[0].plot()
    cv2.imshow("Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
