import pandas as pd
import numpy as np
from random import choice
import requests
import time

# API-Schlüssel
COINMARKETCAL_API_KEY = "sU17gXgo5G5G5Ooe8IaySaZ39311FxKF4baByVRP"
CRYPTOPANIC_API_KEY = "4d84414184e3a7a22be654a0b20ec023be078aa3"

# CoinMarketCal Events abrufen
def get_coinmarketcal_events():
    url = "https://developers.coinmarketcal.com/v1/events"
    headers = {
        'Accept': 'application/json',
        'x-api-key': COINMARKETCAL_API_KEY
    }
    params = {
        'coins': 'bitcoin',
        'max': 5,
        'page': 1
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('body', [])
    else:
        print("Fehler bei CoinMarketCal:", response.status_code)
        return []

# CryptoPanic Nachrichten abrufen
def get_cryptopanic_news():
    url = "https://cryptopanic.com/api/v1/posts/"
    params = {
        'auth_token': CRYPTOPANIC_API_KEY,
        'currencies': 'BTC',
        'kind': 'news',
        'public': 'true'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print("Fehler bei CryptoPanic:", response.status_code)
        return []

# Moving Average berechnen
def calculate_moving_average(data, window=14):
    return data['close'].rolling(window=window).mean()

# RSI berechnen
def calculate_rsi(data, window=14):
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Marktsignal ermitteln
def analyze_btc(events, news):
    if any("hard fork" in event.get('title', '').lower() for event in events):
        return "neutral"
    if any("bearish" in article.get('title', '').lower() for article in news):
        return "short"
    return choice(["long", "short", "neutral"])

# Technische Indikatoren berechnen
def get_technical_indicators(data):
    rsi = calculate_rsi(data)
    moving_avg = calculate_moving_average(data)
    return {
        "rsi": rsi.iloc[-1],
        "moving_avg": moving_avg.iloc[-1],
        "trend": "bullish" if rsi.iloc[-1] > 50 else "bearish"
    }

# BTC-Daten von Binance abrufen
def get_real_btc_data():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        'symbol': 'BTCUSDT',
        'interval': '5m',
        'limit': 100
    }
    response = requests.get(url, params=params)
    data = response.json()
    closes = [float(candle[4]) for candle in data]
    return pd.DataFrame({'close': closes})

# Hauptüberwachung
if __name__ == "__main__":
    while True:
        data = get_real_btc_data()
        tech_indicators = get_technical_indicators(data)
        events = get_coinmarketcal_events()
        news = get_cryptopanic_news()
        signal = analyze_btc(events, news)

        print(f"Signal: {signal}")
        print(f"Technische Indikatoren: {tech_indicators}")

        if signal == "long":
            print("📈 LONG – Kaufsignal")
        elif signal == "short":
            print("📉 SHORT – Verkaufssignal")
        else:
            print("➖ NEUTRAL – Keine Aktion")

        time.sleep(300)  # 5 Minuten
