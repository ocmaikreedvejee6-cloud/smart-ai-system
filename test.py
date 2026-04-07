from ultralytics import YOLO
import cv2

# =========================
# LOAD YOUR TRAINED MODEL
# =========================
model = YOLO("best.pt")  # <-- make sure path is correct

# Print class names (IMPORTANT DEBUG)
print("Model classes:", model.names)

# =========================
# OPEN CAMERA
# =========================
cap = cv2.VideoCapture(0)  # try 0 or "/dev/video0"

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

# =========================
# LOOP
# =========================
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # =========================
    # RUN YOLO DETECTION
    # =========================
    results = model(frame, conf=0.25)

    # =========================
    # DRAW RESULTS
    # =========================
    annotated_frame = results[0].plot()

    # =========================
    # SHOW FRAME
    # =========================
    cv2.imshow("YOLOv8 Detection", annotated_frame)

    # =========================
    # PRINT DETECTED CLASSES
    # =========================
    if results[0].boxes is not None:
        for cls in results[0].boxes.cls:
            class_id = int(cls)
            print("Detected:", model.names[class_id])

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# =========================
# CLEAN UP
# =========================
cap.release()
cv2.destroyAllWindows()
