import time
from discord_notifier import send_discord_message
from event_checker import check_events
from btc_analyzer import analyze_btc, get_technical_indicators, calculate_position_size
from btc_analyzer import get_simulated_data  # Füge die importierte Funktion hinzu

# Beispiel für die Verwendung der Funktionen
btc_analysis_result = analyze_btc()  # Führt die BTC-Analyse durch
technical_indicators = get_technical_indicators(get_simulated_data())  # Holt technische Indikatoren, übergibt die Daten
position_size = calculate_position_size(account_balance, risk_per_trade)  # Berechnet die Positionsgröße

WEBHOOK_URL = "https://discord.com/api/webhooks/1368347672825561218/UlxIyFUDOJm46Vd0fVARlw4hSe6lFTbNXVt-h171BiOY80i_jl79qJLt-_0234Y49sbv"

last_signal = None

# Risikomanagement-Parameter
account_balance = 10000  # Beispiel-Guthaben in USD
risk_per_trade = 0.02  # 2% Risikomanagement pro Trade

while True:
    data = get_simulated_data()  # Hole die simulierten Daten
    signal = analyze_btc()  # Führe die BTC-Analyse durch
    event_info = check_events()
    tech_indicators = get_technical_indicators(data)  # Hole die technischen Indikatoren mit den übergebenen Daten

    # Berechne Positionsgröße
    position_size = calculate_position_size(account_balance, risk_per_trade)  # Übergibt die nötigen Argumente

    if signal != last_signal:
        # Baue detaillierte Nachricht
        message = f"📈 **Neues Signal: {signal.upper()}**\n"
        message += f"- 📊 **Marktanalyse**: Der Markt zeigt eine **{tech_indicators['trend']}** Struktur.\n"
        message += f"- 📉 **Technische Indikatoren**:\n"
        message += f"   - **RSI**: {tech_indicators['rsi']}\n"
        message += f"   - **Moving Avg**: {tech_indicators['moving_avg']}\n"
        message += f"- 💰 **Empfohlene Positionsgröße**: Investiere **{position_size} USD**\n"
        message += f"- ⏳ **Voraussichtliche Handelsdauer**: Halte den Trade für ca. **3 Stunden**\n"
        message += f"- 📍 **Stop-Loss**: Setze deinen Stop-Loss bei **$25,000**\n"
        message += f"- 🎯 **Take-Profit**: Ziel ist **$30,000**\n"

        send_discord_message(WEBHOOK_URL, message)
        last_signal = signal

    if event_info:
        send_discord_message(WEBHOOK_URL, f"📅 **Bevorstehendes Event**: {event_info}")

    time.sleep(300)  # alle 5 Minuten

