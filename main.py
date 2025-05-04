import time
from discord_notifier import send_discord_message
from event_checker import check_events
from btc_analyzer import analyze_btc, get_technical_indicators, calculate_position_size
from btc_analyzer import get_simulated_data  # Füge die importierte Funktion hinzu

# Beispiel für die Verwendung der Funktionen
WEBHOOK_URL = "https://discord.com/api/webhooks/1368347672825561218/UlxIyFUDOJm46Vd0fVARlw4hSe6lFTbNXVt-h171BiOY80i_jl79qJLt-_0234Y49sbv"

last_signal = None
last_message_time = time.time()  # Speichert die Zeit der letzten Nachricht
message_interval = 20 * 60  # 20 Minuten (in Sekunden)

# Risikomanagement-Parameter
account_balance = 10000  # Beispiel-Guthaben in USD
risk_per_trade = 0.02  # 2% Risikomanagement pro Trade

while True:
    data = get_simulated_data()  # Hole die simulierten Daten
    signal = analyze_btc()  # Führe die BTC-Analyse durch
    event_info = check_events()
    tech_indicators = get_technical_indicators(data)  # Hole die technischen Indikatoren mit den übergebenen Daten

    # Überprüfen, ob wir alle 5 Minuten den Markt analysieren und eine Nachricht senden sollen
    current_time = time.time()
    time_since_last_message = current_time - last_message_time

    if time_since_last_message >= message_interval or signal != last_signal:  # Nachricht senden alle 20 Minuten oder bei Änderung des Signals
        # Baue detaillierte Nachricht ohne Positionsgröße, Stop-Loss und Take-Profit
        message = f"📈 **Neues Signal: {signal.upper()}**\n"
        message += f"- 📊 **Marktanalyse**: Der Markt zeigt eine **{tech_indicators['trend']}** Struktur.\n"
        message += f"- 📉 **Technische Indikatoren**:\n"
        message += f"   - **RSI**: {tech_indicators['rsi']}\n"
        message += f"   - **Moving Avg**: {tech_indicators['moving_avg']}\n"
        message += f"- ⏳ **Voraussichtliche Handelsdauer**: Halte den Trade für ca. **3 Stunden**\n"

        # Wenn das Signal "neutral" ist, bedeutet es, dass du den Trade schließen solltest
        if signal == "neutral" and last_signal != "neutral":
            message += f"- ⚠️ **Wichtige Änderung**: Schließe deinen Trade, da das Signal **neutral** ist.\n"

        send_discord_message(WEBHOOK_URL, message)
        last_signal = signal  # Aktualisiere das Signal
        last_message_time = current_time  # Aktualisiere die Zeit der letzten Nachricht

    if event_info:
        send_discord_message(WEBHOOK_URL, f"📅 **Bevorstehendes Event**: {event_info}")

    time.sleep(300)  # alle 5 Minuten den Markt prüfen
