import pandas as pd
import numpy as np
from random import choice

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

# Berechnet die Positionsgröße basierend auf dem Kontostand und dem Risiko
def calculate_position_size(balance, risk_percentage=0.01, stop_loss=0.02):
    """Berechnet die Positionsgröße für den Handel basierend auf dem Kontostand und Risiko-Parametern."""
    position_size = (balance * risk_percentage) / stop_loss
    return position_size

# Simulierte BTC-Daten (kannst du durch echte Daten ersetzen)
def get_simulated_data():
    """Erzeugt zufällige Bitcoin-Daten, die durch echte Marktdaten ersetzt werden können."""
    return pd.DataFrame({
        'close': np.random.randn(100) + 100  # Zufällige Zahlen für den Schlusskurs
    })


# Berechnungen (Beispiel mit simulierten Daten)
data = get_simulated_data()

# Berechnungen
moving_avg = calculate_moving_average(data)
rsi = calculate_rsi(data)

# Beispiel-Ausgabe
print(moving_avg.tail())  # zeigt die letzten 5 Werte des Moving Average
print(rsi.tail())  # zeigt die letzten 5 Werte des RSI

# Beispiel für die Verwendung der get_technical_indicators-Funktion
tech_indicators = get_technical_indicators(data)
print(tech_indicators)  # Zeigt die technischen Indikatoren an
