import requests
from datetime import date, timedelta

def get_events():
    today = date.today()
    end_date = today + timedelta(days=14)

    country = '_country/cl'
    region = '_state/Región%20Metropolitana'
    radius = '_radius/50'
    unit = '_unit/km'
    date_param = f'_start/{today}'
    end_param = f'_end/{end_date}'

    url = f'https://pokedata.ovh/events/api/_tcg/cups/challenges/{country}/{region}/{radius}/{unit}/{date_param}/{end_param}'
    r = requests.get(url)
    return r.json()
