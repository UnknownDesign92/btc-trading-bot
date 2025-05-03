import pandas as pd
import numpy as np

# Beispiel für einfache Moving Average Berechnung
def calculate_moving_average(data, window=14):
    return data['close'].rolling(window=window).mean()

# Beispiel für RSI Berechnung
def calculate_rsi(data, window=14):
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Simulierte BTC-Daten (kannst du durch echte Daten ersetzen)
data = pd.DataFrame({
    'close': np.random.randn(100) + 100  # zufällige Zahlen für den Schlusskurs
})

# Berechnungen
moving_avg = calculate_moving_average(data)
rsi = calculate_rsi(data)

print(moving_avg.tail())  # zeigt den letzten Moving Average Wert
print(rsi.tail())  # zeigt den letzten RSI Wert
