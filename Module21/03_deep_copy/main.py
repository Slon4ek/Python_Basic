import copy
import json

brand = 'телефон'
site = {
    'html': {
        'head': {
            'title': f'Куплю/продам {brand} недорого'
        },
        'body': {
            'h2': f'У нас самая низкая цена на {brand}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def change_brand(data, tag_1, tag_2, product):
    if tag_1 in data:
        data[tag_1] = f'Куплю/продам {product} недорого'
    elif tag_2 in data:
        data[tag_2] = f'У нас самая низкая цена на {product}'
    for key, value in data.items():
        if isinstance(value, dict):
            change_brand(value, tag_1, tag_2, product)
    return data


def create_sites_dict(q_sites, data=None):
    data = data or site
    sites_dict = dict()
    for _ in range(q_sites):
        new_brand = input('Введите название продукта для нового сайта: ')
        sites_dict[new_brand] = change_brand(copy.deepcopy(data), 'title', 'h2', new_brand)
        for key, val in sites_dict.items():
            print(f'Сайт для {key}: \n', json.dumps(val, ensure_ascii=False, indent=4))
    return sites_dict


sites_quantity = int(input('Сколько сайтов: '))
new_sites = create_sites_dict(sites_quantity)
