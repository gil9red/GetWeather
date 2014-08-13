__author__ = 'ipetrash'

import urllib.request
import json

# https://developer.worldweatheronline.com/page/explorer-free
# https://developer.worldweatheronline.com/
# http://www.worldweatheronline.com/Magnitogorsk-weather/Chelyabinsk/RU.aspx

if __name__ == '__main__':
    post_params = {
        'q': 'Magnitogorsk',
        'format': 'json',
        'date': 'today',
        'key': '63bf6ed71f4a52d00ac9f6cf326a76aed49e4791',
    }

    url = "https://api.worldweatheronline.com/free/v1/weather.ashx?" + urllib.parse.urlencode(post_params)
    with urllib.request.urlopen(url) as f:
        json_string = f.read().decode("utf-8")
        parsed_json = json.loads(json_string)
        data = parsed_json["data"]
        current_condition = data["current_condition"][0]
        request = data["request"][0]

        temp_C = current_condition["temp_C"]
        pressure = current_condition["pressure"]

        print("City: '{c}', temp: {t_C}C, pressure: {p}mb".format(c=request["query"], t_C=temp_C, p=pressure), end='')