import time
from discord_notifier import send_discord_message
from event_checker import check_events
from btc_analyzer import analyze_btc, get_technical_indicators, calculate_position_size

# Beispiel für die Verwendung der Funktionen
btc_analysis_result = analyze_btc()  # Führt die BTC-Analyse durch
technical_indicators = get_technical_indicators()  # Holt technische Indikatoren
position_size = calculate_position_size()  # Berechnet die Positionsgröße

WEBHOOK_URL = "https://discord.com/api/webhooks/1368347672825561218/UlxIyFUDOJm46Vd0fVARlw4hSe6lFTbNXVt-h171BiOY80i_jl79qJLt-_0234Y49sbv"

last_signal = None

# Risikomanagement-Parameter
account_balance = 10000  # Beispiel-Guthaben in USD
risk_per_trade = 0.02  # 2% Risikomanagement pro Trade

while True:
    signal = analyze_btc()  # Holt die Analyseergebnisse (long/short/neutral)
    event_info = check_events()  # Überprüft bevorstehende Ereignisse (z. B. Nachrichten)
    tech_indicators = get_technical_indicators()  # Holt technische Indikatoren

    # Berechne Positionsgröße basierend auf Kontostand und Risiko
    position_size = calculate_position_size(account_balance, risk_per_trade)

    if signal != last_signal:  # Wenn sich das Signal geändert hat
        # Baue detaillierte Nachricht für Discord
        message = f"📈 **Neues Signal: {signal.upper()}**\n"
        message += f"- 📊 **Marktanalyse**: Der Markt zeigt eine **{tech_indicators['trend']}** Struktur.\n"
        message += f"- 📉 **Technische Indikatoren**:\n"
        message += f"   - **RSI**: {tech_indicators['rsi']}\n"
        message += f"   - **MACD**: {tech_indicators['macd']}\n"
        message += f"   - **Volumen**: {tech_indicators['volume']}\n"
        message += f"- 💰 **Empfohlene Positionsgröße**: Investiere **{position_size} USD**\n"
        message += f"- ⏳ **Voraussichtliche Handelsdauer**: Halte den Trade für ca. **3 Stunden**\n"
        message += f"- 📍 **Stop-Loss**: Setze deinen Stop-Loss bei **$25,000**\n"
        message += f"- 🎯 **Take-Profit**: Ziel ist **$30,000**\n"

        send_discord_message(WEBHOOK_URL, message)  # Sendet die Nachricht an Discord
        last_signal = signal  # Aktualisiert das letzte Signal

    if event_info:  # Falls es ein bevorstehendes Ereignis gibt
        send_discord_message(WEBHOOK_URL, f"📅 **Bevorstehendes Event**: {event_info}")

    time.sleep(300)  # 5 Minuten warten, bevor der nächste Durchlauf startet
