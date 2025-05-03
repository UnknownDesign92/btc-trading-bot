import talib
import numpy as np
import requests

# Dummy-Daten: Hier musst du Daten von einer API oder einer Datenquelle abrufen.
def get_historical_btc_data():
    # Beispielhafte historische Daten (time, open, high, low, close, volume)
    # Du kannst stattdessen echte Daten von einer API wie Binance oder CoinGecko beziehen.
    return [
        {'timestamp': '2025-05-01', 'close': 27000},
        {'timestamp': '2025-05-02', 'close': 28000},
        {'timestamp': '2025-05-03', 'close': 29000},
        {'timestamp': '2025-05-04', 'close': 30000},
        # Weitere Daten hinzufügen...
    ]

def get_technical_indicators():
    # Hole dir historische BTC-Daten
    historical_data = get_historical_btc_data()

    # Berechnung von Indikatoren mit TA-Lib
    close_prices = np.array([data['close'] for data in historical_data])

    # RSI (Relative Strength Index)
    rsi = talib.RSI(close_prices, timeperiod=14)

    # MACD (Moving Average Convergence Divergence)
    macd, signal, hist = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)

    # Berechne einfache gleitende Durchschnitte (SMA)
    sma_50 = talib.SMA(close_prices, timeperiod=50)
    sma_200 = talib.SMA(close_prices, timeperiod=200)

    indicators = {
        'rsi': rsi[-1],  # Letzter RSI-Wert
        'macd': macd[-1],  # Letzter MACD-Wert
        'sma_50': sma_50[-1],  # Letzter SMA-50-Wert
        'sma_200': sma_200[-1],  # Letzter SMA-200-Wert
    }

    return indicators

def analyze_btc():
    # Holen sich technische Indikatoren
    indicators = get_technical_indicators()

    # Logik für Handelsstrategie basierend auf den Indikatoren
    if indicators['rsi'] < 30 and indicators['macd'] > 0:
        return "long"
    elif indicators['rsi'] > 70 and indicators['macd'] < 0:
        return "short"
    else:
        return "neutral"
