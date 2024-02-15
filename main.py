import os
import sys

import pygame
import requests
from param import size_get

name_object = input('Введите название географического объекта')
data = size_get(name_object)
coords = data[:2]
scale = data[2]
api_server_static = 'https://static-maps.yandex.ru/1.x/'
params_geo = {
    'll': ','.join(coords),
    'spn': scale,
    'l': 'map',
    'pt': ','.join(coords),
}
response = requests.get(api_server_static, params=params_geo)
if response:
    pass
else:
    print("Ошибка выполнения запроса:")
    print(api_server_static)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file_1 = "map.png"
with open(map_file_1, "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file_1), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file_1)
