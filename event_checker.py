import requests

# API-Schlüssel
COINMARKETCAL_API_KEY = "sU17gXgo5G5G5Ooe8IaySaZ39311FxKF4baByVRP"
CRYPTOPANIC_API_KEY = "4d84414184e3a7a22be654a0b20ec023be078aa3"

# Abruf von wichtigen Bitcoin-Ereignissen von CoinMarketCal
def get_coinmarketcal_events():
    """Holt bevorstehende Ereignisse für Bitcoin von CoinMarketCal."""
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
        print("❌ Fehler bei CoinMarketCal:", response.status_code)
        return []

# Abruf der neuesten Bitcoin-Nachrichten von CryptoPanic
def get_cryptopanic_news():
    """Holt aktuelle Bitcoin-Nachrichten von CryptoPanic."""
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
        print("❌ Fehler bei CryptoPanic:", response.status_code)
        return []

# Optional: CoinTelegraph (inaktiv, falls nicht funktionsfähig)
# def get_cointelegraph_news():
#     """(Optional) Holt Bitcoin-Nachrichten von CoinTelegraph – keine offizielle API."""
#     url = "https://api.cointelegraph.com/v1/news"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json().get('data', [])
#     else:
#         print("❌ Fehler bei CoinTelegraph:", response.status_code)
#         return []

# Kombinierter Aufruf aller Datenquellen
def get_important_bitcoin_data():
    """Kombiniert Events und News von CoinMarketCal und CryptoPanic."""
    
    # CoinMarketCal Events
    events = get_coinmarketcal_events()
    print("📅 Bevorstehende Ereignisse von CoinMarketCal:")
    for event in events:
        title = event.get('title', 'Kein Titel')
        date = event.get('date_event', 'Kein Datum')
        print(f"- {title} am {date}")

    # CryptoPanic News
    news = get_cryptopanic_news()
    print("\n📰 Neueste Bitcoin-Nachrichten von CryptoPanic:")
    for article in news:
        print(f"- {article.get('title', 'Kein Titel')}")

    # CoinTelegraph (deaktiviert)
    # cointelegraph_news = get_cointelegraph_news()
    # print("\n🗞️ Nachrichten von CoinTelegraph:")
    # for article in cointelegraph_news:
    #     print(f"- {article.get('title', 'Kein Titel')}")

# Direkter Aufruf zum Testen
if __name__ == "__main__":
    get_important_bitcoin_data()
# Wrapper-Funktionen für main.py
def get_events():
    return get_coinmarketcal_events()

def get_news():
    return get_cryptopanic_news()
