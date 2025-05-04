import requests

# Funktion zum Senden einer Nachricht an Discord
def send_discord_message(webhook_url, message):
    """Sendet eine Nachricht an Discord über den Webhook."""
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Fehler beim Senden der Nachricht: {response.status_code}")
