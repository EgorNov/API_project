import requests
from requests import post
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
        return long, lat

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
        resp = requests.get(map_request, params=params)

        if not resp:
            print("Ошибка выполнения запроса:")
    except Exception:
        print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(resp.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    skill_id = 'ff930959-af59-4b76-ac73-688158f4dcbf'
    token = 'AQAAAAADXyKXAAT7o0qDFWCp6EyPr0JuYtnKxjM'
    url = f'https://dialogs.yandex.net/api/v1/skills/{skill_id}/images'
    files = {'file': resp.content}
    headers = {'Authorization': f'OAuth {token}'}
    s = post(url, files=files, headers=headers)
    picture_code = s.json()['image']['id']

    return picture_code
