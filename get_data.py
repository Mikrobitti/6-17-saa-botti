from get_time import get_time
import requests

def get_data(url, location, req_type):

    timestamp = ""

    #Different time delays for different queries
    if req_type == "get_weather_data":
        timestamp = get_time(20)

    data = requests.get(url+location+"&starttime="+timestamp)
    print(url+location+"&starttime="+timestamp)
    return data.text