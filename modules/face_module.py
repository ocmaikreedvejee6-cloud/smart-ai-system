import face_recognition
import cv2

known_encodings = []
known_names = []

def load_known_faces():
    image = face_recognition.load_image_file("known_faces/owner.jpg")
    encoding = face_recognition.face_encodings(image)[0]

    known_encodings.append(encoding)
    known_names.append("Owner")

def check_face(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding in encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)

        if True in matches:
            return "known"

    return "unknown"
