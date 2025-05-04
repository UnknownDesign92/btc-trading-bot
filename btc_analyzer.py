import pandas as pd
import numpy as np
from random import choice
import requests
import time

# Beispiel für einfache Moving Average Berechnung
def calculate_moving_average(data, window=14):
    """Berechnet den gleitenden Durchschnitt (Moving Average) der BTC-Daten."""
    return data['close'].rolling(window=window).mean()

# Beispiel für RSI Berechnung
def calculate_rsi(data, window=14):
    """Berechnet den RSI (Relative Strength Index) der BTC-Daten."""
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Die Funktion, die die BTC-Analyse durchführt (hier als Platzhalter)
def analyze_btc():
    """Führt eine zufällige Analyse des Bitcoin-Markts durch und gibt ein Signal zurück."""
    return choice(["long", "short", "neutral"])

# Holt technische Indikatoren (RSI und Moving Average)
def get_technical_indicators(data):
    """Gibt technische Indikatoren wie RSI und Moving Average zurück."""
    rsi = calculate_rsi(data)
    moving_avg = calculate_moving_average(data)
    
    # Hier erstellen wir ein Dictionary, das die technischen Indikatoren enthält
    tech_indicators = {
        "rsi": rsi.iloc[-1],  # den letzten Wert des RSI
        "moving_avg": moving_avg.iloc[-1],  # den letzten Wert des Moving Average
        "trend": "bullish" if rsi.iloc[-1] > 50 else "bearish"  # Trend basierend auf RSI
    }
    return tech_indicators

# Holt echte Bitcoin-Daten von Binance (5-Minuten Intervalle)
def get_real_btc_data():
    """Holt echte Bitcoin-Daten von Binance."""
    url = "https://api.binance.com/api/v3/klines"
    params = {
        'symbol': 'BTCUSDT',
        'interval': '5m',  # 5-Minuten-Intervalle
        'limit': 100  # Letzte 100 Kerzen
    }
    response = requests.get(url, params=params)
    data = response.json()
    closes = [float(candle[4]) for candle in data]  # Der Schlusspreis ist an der 5. Stelle
    return pd.DataFrame({'close': closes})

# Berechnungen (Beispiel mit echten Daten von Binance)
data = get_real_btc_data()  # Hole die echten Daten von Binance

# Berechnungen
moving_avg = calculate_moving_average(data)
rsi = calculate_rsi(data)

# Beispiel-Ausgabe
print(moving_avg.tail())  # zeigt die letzten 5 Werte des Moving Average
print(rsi.tail())  # zeigt die letzten 5 Werte des RSI

# Beispiel für die Verwendung der get_technical_indicators-Funktion
tech_indicators = get_technical_indicators(data)
print(tech_indicators)  # Zeigt die technischen Indikatoren an

# Simuliere eine kontinuierliche Marktüberwachung (z.B. alle 5 Minuten):
while True:
    data = get_real_btc_data()  # Hole die neuesten echten Marktdaten von Binance
    tech_indicators = get_technical_indicators(data)
    signal = analyze_btc()  # Führe die BTC-Analyse durch und bekomme ein Signal

    # Ausgabe der Ergebnisse
    print(f"Signal: {signal}")
    print(f"Technische Indikatoren: {tech_indicators}")

    # Überprüfe, ob das Signal sich geändert hat oder ob es eine neue Nachricht geben soll
    if signal == "long":
        print("Signal ist Long – Bereit zu handeln.")
    elif signal == "short":
        print("Signal ist Short – Bereit zu handeln.")
    elif signal == "neutral":
        print("Signal ist Neutral – Keine Aktion notwendig.")

    # Warte 5 Minuten, bevor die Daten erneut abgefragt werden
    time.sleep(300)  # alle 5 Minuten
