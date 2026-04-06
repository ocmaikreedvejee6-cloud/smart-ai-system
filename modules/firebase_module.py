import firebase_admin
from firebase_admin import credentials, db, storage
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOUR_DB_URL',
    'storageBucket': 'YOUR_BUCKET.appspot.com'
})

def upload_image(path, name):
    bucket = storage.bucket()
    blob = bucket.blob(f"intruders/{name}")
    blob.upload_from_filename(path)
    blob.make_public()
    return blob.public_url

def save_log(event, image_url):
    ref = db.reference("logs")
    ref.push({
        "event": event,
        "image": image_url,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
