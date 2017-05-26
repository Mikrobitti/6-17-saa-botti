from get_data import get_data
import os
import xml.etree.ElementTree as ET
import collections

FMI_API_KEY = os.environ['FMI_API_KEY']
WIT_APP_KEY = os.environ['WIT_APP_KEY']
WIT_SERVER_ACCESS_TOKEN = os.environ['WIT_SERVER_ACCESS_TOKEN']
WIT_AI_URL = "https://api.wit.ai/message?v=20170502&q="

weather_now_url = "http://data.fmi.fi/fmi-apikey/" + FMI_API_KEY + "/wfs?request=getFeature&storedquery_id=fmi::observations::weather::simple&place="

def get_weather_data(location):
    data = get_data(weather_now_url, location, "get_weather_data")
    root = ET.fromstring(data)

    weather_dictionary = collections.OrderedDict()

    for member in root.iter('{http://www.opengis.net/wfs/2.0}member'):

        for BsWfsElement in member.iter('{http://xml.fmi.fi/schema/wfs/2.0}BsWfsElement'):

            for ParameterName in BsWfsElement.iter('{http://xml.fmi.fi/schema/wfs/2.0}ParameterName'):

                parameter_name = ParameterName.text
            for ParameterValue in BsWfsElement.iter('{http://xml.fmi.fi/schema/wfs/2.0}ParameterValue'):

                parameter_value = ParameterValue.text

            weather_dictionary[parameter_name] = parameter_value

    return weather_dictionary
