import json
import requests


def pilots_info(url):
    result = requests.get(url).json()
    return {'name': result['name'],
            'height': result['height'],
            'mass': result['mass'],
            'homeworld': planet_info(result['homeworld']),
            'homeworld_url': result['homeworld']
            }


def planet_info(url):
    result = requests.get(url).json()
    return result['name']


def search_info(ship_name):
    lst = ['starships', 'planets', 'films', 'species', 'vehicles', 'people']
    ship_info = dict()
    for i_inf in lst:
        result = requests.get(f'https://swapi.dev/api/{i_inf}/?search={ship_name}').json()
        if result['results']:
            result = result['results'][0]
            ship_info['ship_name'] = result['name']
            ship_info['max_atmosphering_speed'] = result['max_atmosphering_speed']
            ship_info['starship_class'] = result['starship_class']
            ship_info['pilots'] = [pilots_info(pilot) for pilot in result['pilots']]
            return ship_info


res = search_info('millen')
with open('ship_info.json', 'w') as file:
    json.dump(search_info('millen'), file, indent=4)
print(json.dumps(res, ensure_ascii=False, indent=4))
