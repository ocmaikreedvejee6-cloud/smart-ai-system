import cv2
import time
from ultralytics import YOLO

Modules

from stream_module import start_stream, update_frame
from face_module import recognize_face
from relay_module import setup_gpio, turn_on, turn_off
from telegram_module import send_alert

==========================

LOAD MODEL

==========================

model = YOLO("best.pt")

==========================

SETUP

==========================

cap = cv2.VideoCapture(0)
start_stream()
setup_gpio()

==========================

SETTINGS

==========================

DELAY_OFF = 5
ALERT_COOLDOWN = 10

last_seen = time.time()
last_alert = 0

==========================

MAIN LOOP

==========================

while True:
ret, frame = cap.read()
if not ret:
break

# Resize for performance
frame = cv2.resize(frame, (480, 360))

# Send to stream
update_frame(frame)

# ==========================
# YOLO DETECTION
# ==========================
results = model(frame, verbose=False)[0]

person_detected = False

for box in results.boxes:
    if int(box.cls[0]) == 0:  # person class
        person_detected = True
        break

# ==========================
# FACE RECOGNITION
# ==========================
face_status = "unknown"

if person_detected:
    face_status = recognize_face(frame)

# ==========================
# RELAY CONTROL
# ==========================
if person_detected:
    turn_on()
    last_seen = time.time()
else:
    if time.time() - last_seen > DELAY_OFF:
        turn_off()

# ==========================
# TELEGRAM ALERT
# ==========================
now = time.time()

if person_detected and face_status == "unknown":
    if now - last_alert > ALERT_COOLDOWN:
        print("🚨 Intruder detected!")
        send_alert(frame)
        last_alert = now

# ==========================
# DISPLAY
# ==========================
annotated = results.plot()
cv2.imshow("Smart AI System", annotated)

if cv2.waitKey(1) & 0xFF == 27:
    break

==========================

CLEANUP

==========================

cap.release()
cv2.destroyAllWindows()
