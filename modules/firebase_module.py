import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-ai-system-8e589-default-rtdb.firebaseio.com/'
})

def save_log(event):
    ref = db.reference("logs")
    ref.push({
        "event": event,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
