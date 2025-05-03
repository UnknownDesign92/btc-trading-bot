
def check_events():
    from datetime import datetime

    now = datetime.now()
    # Beispiel: FOMC heute um 20 Uhr
    event_time = now.replace(hour=20, minute=0, second=0, microsecond=0)
    if now.date() == event_time.date() and now.hour == 19:
        return "🔔 Morgen FOMC-Meeting um 20:00 Uhr (MEZ). Achtung auf Volatilität."
    return None
