import time
from discord_notifier import send_discord_message
from event_checker import check_events
from btc_analyzer import analyze_btc

WEBHOOK_URL = "https://discord.com/api/webhooks/1368347672825561218/UlxIyFUDOJm46Vd0fVARlw4hSe6lFTbNXVt-h171BiOY80i_jl79qJLt-_0234Y49sbv"

last_signal = None

while True:
    signal = analyze_btc()
    event_info = check_events()

    if signal != last_signal:
        send_discord_message(WEBHOOK_URL, f"📈 Neues Signal: **{signal.upper()}**")
        last_signal = signal

    if event_info:
        send_discord_message(WEBHOOK_URL, f"📅 Bevorstehendes Event: {event_info}")

    time.sleep(300)  # alle 5 Minuten
