import time
from discord_notifier import send_discord_message
from event_checker import get_events, get_news
from btc_analyzer import get_btc_data, calculate_indicators, generate_signal

WEBHOOK_URL = "https://discord.com/api/webhooks/..."  # Deine Discord Webhook-URL
last_signal = None
last_message_time = time.time()  # Zeit der letzten Nachricht
message_interval = 20 * 60  # 20 Minuten (in Sekunden)

while True:
    # Hole die Bitcoin-Marktdaten und berechne technische Indikatoren
    df = get_btc_data()
    df = calculate_indicators(df)
    
    # Generiere ein Handelssignal
    signal = generate_signal(df)

    # Hole bevorstehende Ereignisse und Nachrichten
    events = get_events()
    news = get_news()

    # Baue die Nachricht
    message = f"📈 **Neues Signal: {signal.upper()}**\n"
    message += f"- 📊 **Technische Indikatoren**:\n"
    message += f"   - **RSI**: {df['rsi'].iloc[-1]}\n"
    message += f"   - **SMA (14-Tage)**: {df['sma'].iloc[-1]}\n"
    message += f"- ⏳ **Voraussichtliche Handelsdauer**: Halte den Trade für ca. **3 Stunden**\n"

    if signal == "neutral":
        message += f"- ⚠️ **Wichtige Änderung**: Schließe deinen Trade, da das Signal **neutral** ist.\n"

    # Füge Nachrichten und Ereignisse hinzu, falls sie vorhanden sind
    if events:
        event_info = "\n".join([event['title'] for event in events])  # Zeigt Titel der Ereignisse
        message += f"📅 **Bevorstehende Ereignisse**:\n{event_info}\n"

    if news:
        news_info = "\n".join([article['title'] for article in news])  # Zeigt Titel der neuesten Nachrichten
        message += f"📰 **Neueste Nachrichten**:\n{news_info}\n"

    # Sende die Nachricht an Discord
    current_time = time.time()
    time_since_last_message = current_time - last_message_time
    if time_since_last_message >= message_interval or signal != last_signal:
        send_discord_message(WEBHOOK_URL, message)
        last_signal = signal  # Aktualisiere das Signal
        last_message_time = current_time  # Aktualisiere die Zeit der letzten Nachricht

    time.sleep(300)  # Alle 5 Minuten den Markt prüfen

