import requests
import os
import json
import libvoikko
v = libvoikko.Voikko(u"fi")

from get_weather_data import get_weather_data

WIT_SERVER_ACCESS_TOKEN = os.environ['WIT_SERVER_ACCESS_TOKEN']
WIT_AI_URL = "https://api.wit.ai/message?v=20170502&q="

def get_basic_form(location):
    word_analysis = v.analyze(location)
    print (word_analysis)
    for analyse in word_analysis:
        if analyse['CLASS'] == 'paikannimi':
            return analyse['BASEFORM']
    return 'NOT FOUND'

def parse_response(weather_dictionary):
    weather_response = ""
    for parameter, value in weather_dictionary.items():
        weather_response += parameter + " " + value + " "
    if weather_response == "":
        return "Ei tietoja saatavilla"
    else:
        return weather_response

def main():
    # Luetaan käyttäjän syöte. Käytettäessä jotakin chatalustaa syöte saataisiin sieltä.
    user_input = input("> ")

    # Lähetetään syöte analysoitavaksi wit.ai:lle.
    headers = {'Authorization': 'Bearer '+ WIT_SERVER_ACCESS_TOKEN}
    response = requests.get(WIT_AI_URL+user_input, headers=headers)
    response_json = json.loads(response.text)

    # Luetaan wit.ai:n vastaus ja otetaan sieltä saatu aie talteen.
    intent = response_json['entities']['intent'][0]['value']
    print (intent)
    # Luetaan wit.ai:n vastaus ja otetaan sieltä saatu paikkatieto talteen.
    location_raw = response_json['entities']['location'][0]['value']
    # Syötetään saatu paikkatieto voikolle sijamuodoista eroon pääsemiseksi.
    location = get_basic_form(location_raw)

    # Saadun aikeen mukaan haetaan joko normaalit säätiedot tai ilmanlaatutiedot
    if intent == 'weather':
        weather_dictionary = get_weather_data(location)
        print(parse_response(weather_dictionary))
    else: 
        print("Aietta ei tunnistettu")

main()