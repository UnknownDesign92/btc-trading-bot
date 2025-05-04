import requests

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

# Abruf von Bitcoin-Nachrichten aus CoinTelegraph
def get_cointelegraph_news():
    """Holt Bitcoin-Nachrichten von CoinTelegraph."""
    url = "https://api.cointelegraph.com/v1/news"
    response = requests.get(url)
    if response.status_code == 200:
        news = response.json()
        return news['data']  # Rückgabe der Nachrichten
    else:
        print("Fehler beim Abrufen der CoinTelegraph-Nachrichten:", response.status_code)
        return []

# Beispiel, wie du alle wichtigen Quellen abfragst und die Daten verarbeitest
def get_important_bitcoin_data():
    """Kombiniert alle Daten von Ereignissen und Nachrichtenquellen."""
    # Abruf von Ereignissen von CoinMarketCal
    events = get_coinmarketcal_events()
    print("Bevorstehende Ereignisse von CoinMarketCal:")
    for event in events:
        print(f"- {event['name']} am {event['date']}")

    # Abruf der Nachrichten von CryptoPanic
    news = get_cryptopanic_news()
    print("\nNeueste Bitcoin-Nachrichten von CryptoPanic:")
    for article in news:
        print(f"- {article['title']}")

    # Abruf von Nachrichten von CoinTelegraph
    cointelegraph_news = get_cointelegraph_news()
    print("\nNeueste Bitcoin-Nachrichten von CoinTelegraph:")
    for article in cointelegraph_news:
        print(f"- {article['title']}")

# Hauptprogramm: Automatische Abfrage der wichtigen Bitcoin-Daten
if __name__ == "__main__":
    get_important_bitcoin_data()
