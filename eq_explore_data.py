import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
from plotly import colors


# Просмотр встроенных в 'plotly' цветовых шкал для диаграмм:
for k, v in colors.PLOTLY_SCALES.items():
    print(k, v)

# Форматирование файла в читабельный ниже. "indent" - форматирует данные с отступами, соответствующими структуре данных:
# with open('data/eq_1_day_m1.json') as f:
#     all_data = json.load(f)
# with open('data/eq_1_readable.json', 'w') as f:
#     json.dump(all_data, f, indent=4)

with open('data/eq_1_readable.json') as f:
    all_data = json.load(f)

all_dicts = all_data['features']
mags, lons, lats, places = [], [], [], []

# Упражнение 16.6 по рефакторингу выполнено ниже:
for d in all_dicts:
    lons.append(d['geometry']['coordinates'][0])
    lats.append(d['geometry']['coordinates'][1])
    places.append(d['properties']['place'])
    mags.append(d['properties']['mag'])

# Нанесение данных на карту:
# data = [Scattergeo(lon=lons, lat=lats)]  # Список, ибо можно нанести более одного набора данных при желании.
# В случае ключа 'marker' - обязательно, чтобы был словарь. Список работать не будет.
data = [{'type': 'scattergeo',
         'text': places,  # Вывод текстового местоположения(помимо долготы/широты) при наведении на точку землетрясения.
         'lon': lons,
         'lat': lats,
         'marker': {'size': [5 * mag for mag in mags],
                    'color': mags,
                    'colorscale': 'Electric',
                    'reversescale': True,
                    'colorbar': {'title': 'Magnitude'},
                    'opacity': 1}}]  # "opacity" - регулирует прозрачность объекта. Маркер поверх карты.

# Упражнение 16.7 по автоматизации заголовка:
title = all_data['metadata']['title']
my_layout = Layout(title=title)

# Рисуем карту:
offline.plot({'data': data, 'layout': my_layout}, filename='pictures_of_graphs/eq_magnitude.html')
