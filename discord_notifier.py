
import requests

def send_discord_message(webhook_url, content):
    data = {"content": content}
    try:
        requests.post(webhook_url, json=data)
    except Exception as e:
        print("Fehler beim Senden an Discord:", e)
