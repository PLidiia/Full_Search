import sys

import requests


def size_get(toponym_name):
    api_server = "http://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_name,
        "format": "json"}
    response = requests.get(api_server, params=params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        coord_1, coord2 = toponym_coodrinates.split(' ')
        extreme_start_x = float(toponym['boundedBy']['Envelope']['lowerCorner'].split()[0])
        extreme_finish_x = float(toponym['boundedBy']['Envelope']['upperCorner'].split()[0])
        extreme_start_y = float(toponym['boundedBy']['Envelope']['lowerCorner'].split()[1])
        extreme_finish_y = float(toponym['boundedBy']['Envelope']['upperCorner'].split()[1])
        scale = str((abs(extreme_finish_x - extreme_start_x))) + ',' + str(abs(extreme_finish_y - extreme_start_y))
        return [str(coord_1), str(coord2), scale]
    else:
        print("Ошибка выполнения запроса:")
        print(response)
        print("Http статус:", response.status_code, "(", response.reason,
              ")")
        sys.exit(1)
