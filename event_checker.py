import requests

# Abruf bevorstehender Ereignisse von CoinMarketCal
def get_events():
    """Holt bevorstehende Ereignisse für Bitcoin (Hard Forks, Upgrades, etc.)."""
    url = "https://api.coinmarketcal.com/v1/events"
    params = {'coin': 'bitcoin'}
    response = requests.get(url, params=params)
    events = response.json()  # Liste von Ereignissen
    return events

# Abruf der neuesten Bitcoin-Nachrichten von Crypto News API
def get_news():
    """Holt die neuesten Bitcoin-Nachrichten von Crypto News API."""
    url = "https://cryptonews-api.com/api/v1/category"
    params = {'category': 'bitcoin', 'token': 'dein_api_token'}  # Ersetze 'dein_api_token'
    response = requests.get(url, params=params)
    news = response.json()  # Liste von Nachrichten
    return news
