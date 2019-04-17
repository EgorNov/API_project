from flask import Flask, request
import logging
import json
from geo import get_geo_info, get_picture
from cities1 import city_arr

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, filename='app.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
sessionStorage = {}
all_cities = city_arr[:]
print(all_cities)


@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Request: %r', response)
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']
    if req['session']['new']:
        logging.warning(user_id)
        sessionStorage[user_id] = {}
        sessionStorage[user_id]['first_name'] = None
        logging.warning(sessionStorage)
        res['response']['text'] = \
            'Привет! Я могу играть с тобой в города! Учти что я знаю только русские города.' + '\nНазови свое имя.'
        return
    logging.warning('1')
    logging.warning(sessionStorage)
    if sessionStorage[user_id]['first_name'] is None:
        for entity in req['request']['nlu']['entities']:
            if entity['type'] == 'YANDEX.FIO':
                sessionStorage[user_id]['first_name'] = entity['value'].get('first_name', None)
                break
        logging.warning('2')
        logging.warning(sessionStorage)
        if sessionStorage[user_id]['first_name'] is None:
            res['response']['text'] = \
                'Не расслышала имя, повтори.'
        else:
            sessionStorage[user_id]['first_name'] = sessionStorage[user_id]['first_name'].title()
            res['response']['text'] = \
                'Приятно познакомиться, ' + sessionStorage[user_id]['first_name'] + '. Ты начинаешь!'
        return

    cities = get_cities(req)
    if not cities:
        res['response']['text'] = sessionStorage[user_id]['first_name'] + ', ты не написал название города!'
    elif len(cities) == 1:
        logging.warning('а')
        if cities[0] in all_cities:
            logging.warning('б')
            if cities[0] in city_arr:
                logging.warning('в')
                city_arr.pop(city_arr.index(cities[0]))
                city = get_city(cities[0][-1])
                if city:
                    res['response']['card'] = {}
                    res['response']['card']['type'] = 'BigImage'
                    res['response']['card']['title'] = 'Это ' + city.title() + ' на карте, твоя очередь'
                    res['response']['card']['image_id'] = get_picture(get_geo_info(city))
                    logging.warning('г')
                    if get_city(city[-1], alice=True):
                        res['response']['text'] = city.title() + ', тебе на ' + city[-1]
                    else:
                        res['response']['text'] = city.title() + '. На ' + city[-1] + ' больше нет городов, я победила)'
                else:
                    res['response']['text'] = 'Я сдаюсь, ты победил('

            else:
                res['response']['text'] = sessionStorage[user_id]['first_name'] + ', этот город был! Попробуй другой)'
        else:
            res['response']['text'] = sessionStorage[user_id][
                                          'first_name'] + ', я не знаю такого города! Попробуй другой)'
    else:
        res['response']['text'] = sessionStorage[user_id]['first_name'] + ', слишком много городов!'
    return


def get_city(letter, alice=False):
    for i in range(len(city_arr)):
        if city_arr[i][0] == letter:
            if alice:
                return city_arr[i]
            else:
                return city_arr.pop(i)
    return None


def get_cities(req):
    cities = []
    for entity in req['request']['nlu']['entities']:
        if entity['type'] == 'YANDEX.GEO':
            if 'city' in entity['value']:
                cities.append(entity['value']['city'])
    return cities


if __name__ == '__main__':
    app.run()
