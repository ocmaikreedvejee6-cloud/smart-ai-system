from flask import Flask, Response
import cv2
import threading

Initialize Flask app

app = Flask(name)

==========================

Shared frame (global)

==========================

output_frame = None
lock = threading.Lock()

==========================

UPDATE FRAME FROM main.py

==========================

def update_frame(frame):
global output_frame
with lock:
output_frame = frame.copy()

==========================

GENERATE STREAM

==========================

def generate():
global output_frame

while True:
    with lock:
        if output_frame is None:
            continue

        # Encode frame as JPEG
        (flag, encodedImage) = cv2.imencode(".jpg", output_frame)

        if not flag:
            continue

    # Yield frame to browser
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' +
           bytearray(encodedImage) +
           b'\r\n')

==========================

ROUTE

==========================

@app.route("/video")
def video_feed():
return Response(generate(),
mimetype="multipart/x-mixed-replace; boundary=frame")

==========================

RUN SERVER (THREAD)

==========================

def run_server():
app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

def start_stream():
t = threading.Thread(target=run_server)
t.daemon = True
t.start()
