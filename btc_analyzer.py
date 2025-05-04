import pandas as pd
import numpy as np
from random import choice
import requests
import time

# Abruf von wichtigen Bitcoin-Ereignissen von CoinMarketCal
def get_coinmarketcal_events():
    """Holt bevorstehende Ereignisse für Bitcoin (Hard Forks, Upgrades, etc.) von CoinMarketCal."""
    url = "https://api.coinmarketcal.com/v1/events"
    params = {'coin': 'bitcoin'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        events = response.json()  # Liste der Ereignisse
        return events['data']  # Rückgabe der Ereignisse
    else:
        print("Fehler beim Abrufen der CoinMarketCal-Ereignisse:", response.status_code)
        return []

# Abruf der neuesten Bitcoin-Nachrichten von CryptoPanic
def get_cryptopanic_news():
    """Holt die neuesten Bitcoin-Nachrichten von CryptoPanic."""
    url = "https://cryptopanic.com/api/v1/posts/"
    params = {
        'filter': 'bitcoin',  # Filter für Bitcoin-Nachrichten
        'auth_token': 'dein_api_token'  # Dein Authentifizierungstoken für CryptoPanic
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        news = response.json()
        return news['results']  # Rückgabe der Nachrichten
    else:
        print("Fehler beim Abrufen der CryptoPanic-Nachrichten:", response.status_code)
        return []

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
def analyze_btc(events, news):
    """Führt eine Analyse des Bitcoin-Markts durch und gibt ein Signal zurück unter Berücksichtigung von Ereignissen und Nachrichten."""
    if any(event['name'] == 'Bitcoin Hard Fork' for event in events):  # Beispiel für Hard Forks
        return "neutral"  # Neutral, weil Hard Forks den Markt destabilisieren können.
    
    if any("bearish" in article['title'].lower() for article in news):
        return "short"  # Short-Signal aufgrund negativer Nachrichten

    return choice(["long", "short", "neutral"])  # Zufälliges Signal als Platzhalter

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
    
    # Hole Nachrichten und Ereignisse
    events = get_coinmarketcal_events()  # Hole die bevorstehenden Ereignisse
    news = get_cryptopanic_news()  # Hole die neuesten Nachrichten

    # Führe die BTC-Analyse unter Berücksichtigung der Ereignisse und Nachrichten durch
    signal = analyze_btc(events, news)  # Führe die BTC-Analyse durch und bekomme ein Signal

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
