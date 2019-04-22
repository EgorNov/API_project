import requests
import logging
from requests import post
from cities1 import country_codes
import sys


def get_geo_info(city_name):
    try:
        url = "https://geocode-maps.yandex.ru/1.x/"
        params = {
            'geocode': city_name,
            'format': 'json'
        }
        data = requests.get(url, params).json()
        # все отличие тут, мы получаем имя страны
        coordinates_str = data['response']['GeoObjectCollection'][
            'featureMember'][0]['GeoObject']['Point']['pos']
        # Превращаем string в список, так как точка -
        # это пара двух чисел - координат
        long, lat = map(float, coordinates_str.split())
        # Вернем ответ

        return str(long), str(lat)

    except Exception as e:
        return e


def get_picture(coords):
    try:

        map_request = "http://static-maps.yandex.ru/1.x/"
        lon, lat = coords

        params = {
            "ll": ",".join([lon, lat]),
            "z": "10",
            "l": "map"
        }

        response = requests.get(map_request, params=params)

        if not response:
            print("Ошибка выполнения запроса:")
    except Exception:
        print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
        sys.exit(1)

    # Запишем полученное изображение в файл.

    skill_id = 'ff930959-af59-4b76-ac73-688158f4dcbf'
    token = 'AQAAAAADXyKXAAT7o0qDFWCp6EyPr0JuYtnKxjM'
    url = f'https://dialogs.yandex.net/api/v1/skills/{skill_id}/images'
    files = {'file': response.content}

    headers = {'Authorization': f'OAuth {token}'}
    s = post(url, files=files, headers=headers)
    picture_code = s.json()['image']['id']

    return picture_code


def get_city_name(city_name):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        'geocode': city_name,
        'format': 'json'
    }
    data = requests.get(url, params).json()
    country_code = data['response']['GeoObjectCollection'][
        'featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData'][
        'Address']['country_code'].lower()
    url1 = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    api_key = 'trnsl.1.1.20190410T140331Z.9d0a5983cb2980db.acc9b5cefdb3a1e225c8180a04bfdfeaa332f600'
    if country_code not in country_codes and country_code != 'us' and country_code != 'gb' or country_code == 'ru':
        return None
    if country_code == 'us':
        country_code = 'en'
    if country_code == 'gb':
        country_code = 'en'
    params = {
        'key': api_key,
        'text': city_name,
        'lang': 'ru-' + country_code.lower()
    }

    city_name = requests.get(url1, params).json()['text'][0]
    return city_name
