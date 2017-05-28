# get_data.py
# Tiedostossa suoritetaan varsinainen datan hakeminen ilmatieteenlaitoksen
# rajapinnasta

from get_time import get_time
import requests

def get_data(url, location, req_type):

    timestamp = ""

    # FMI:n rajapintaa lisää tutkimalla on varmasti mahdollista löytää tapa, jolla
    # tuoreet havainnot sää muuten kuin kyselyyn viivettä lisäämällä
    if req_type == "get_weather_data":
        timestamp = get_time(20)

    data = requests.get(url+location+"&starttime="+timestamp)
    print(url+location+"&starttime="+timestamp)
    return data.text