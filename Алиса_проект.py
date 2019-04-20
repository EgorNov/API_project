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
    global city_arr
    user_id = req['session']['user_id']
    if req['session']['new']:
        logging.warning(user_id)
        sessionStorage[user_id] = {}
        sessionStorage[user_id]['first_name'] = None
        sessionStorage[user_id]['last'] = None
        sessionStorage[user_id]['end'] = False
        logging.warning(sessionStorage)
        res['response']['text'] = \
            'Привет! Я могу играть с тобой в города! Учти что я знаю только русские города.' + '\nНазови свое имя.'
        return
    logging.warning(sessionStorage)
    if sessionStorage[user_id]['first_name'] is None:
        for entity in req['request']['nlu']['entities']:
            if entity['type'] == 'YANDEX.FIO':
                sessionStorage[user_id]['first_name'] = entity['value'].get('first_name', None)
                break
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
    if sessionStorage[user_id]['end']:
        for i in ['хорошо', 'ладно','давай','да']:
            if i in req['request']['original_utterance'].lower():
                sessionStorage[user_id]['end'] = False
                sessionStorage[user_id]['last'] = None
                city_arr = all_cities[:]
                res['response']['text'] = 'Хорошо ' + sessionStorage[user_id]['first_name'] + '. Ты начинаешь!'
            else:
                res['response']['text'] = 'Ну и ладно'
                res['response']['end_session'] = True
            return
    if not cities:
        res['response']['text'] = sessionStorage[user_id]['first_name'] + ', ты не написал название города!'
    elif len(cities) == 1:
        if cities[0][0] == sessionStorage[user_id]['last'] or sessionStorage[user_id]['last'] is None:
            if cities[0] in all_cities:
                if cities[0] in city_arr:
                    city_arr.pop(city_arr.index(cities[0]))
                    if cities[0][-1] == 'ь'or cities[0][-1] == 'ы':
                        city = get_city(cities[0][-2])
                    else:
                        city = get_city(cities[0][-1])
                    if city:
                        res['response']['card'] = {}
                        res['response']['card']['type'] = 'BigImage'
                        res['response']['card']['image_id'] = get_picture(get_geo_info(city))
                        res['response']['text'] = 'Здесь должна была быть картинка города ' + city.title()
                        if city[0][-1] == 'ь'or city[0][-1] == 'ы':
                            if get_city(city[-1], alice=True):
                                x = city.title() + ', тебе на ' + city[-2]
                                sessionStorage[user_id]['last'] = city[-2]
                            else:
                                x = city.title() + '. На ' + city[-2] + ' больше нет городов, я победила)\n Хочешь сыграть еще?'
                                sessionStorage[user_id]['end'] = True
                        else:
                            if get_city(city[-1], alice=True):
                                x = city.title() + ', тебе на ' + city[-1]
                                sessionStorage[user_id]['last'] = city[-1]
                            else:
                                x = city.title() + '. На ' + city[-1] + ' больше нет городов, я победила)\n Хочешь сыграть еще?'
                                sessionStorage[user_id]['end'] = True


                        logging.warning(x)
                        res['response']['card']['title'] = x
                    else:
                        res['response']['text'] = 'Я сдаюсь, ты победил('
                        sessionStorage[user_id]['end'] = True


                else:
                    res['response']['text'] = sessionStorage[user_id]['first_name'] + ', этот город был! Попробуй другой)'
            else:
                res['response']['text'] = sessionStorage[user_id][
                                          'first_name'] + ', я не знаю такого города! Попробуй другой)'
        else:
             res['response']['text'] = 'Город должен быть на букву ' + sessionStorage[user_id]['last']
    else:
        res['response']['text'] = sessionStorage[user_id]['first_name'] + ', слишком много городов!'
    logging.warning(2)
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
