import requests

TOKEN = "8490765768:AAFU-Vpi0HAiS5_2V2mcboWYeiG8W4neiVE"
CHAT_ID = "437470295"

def send_alert(image_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    
    with open(image_path, "rb") as photo:
        requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"photo": photo}
        )
