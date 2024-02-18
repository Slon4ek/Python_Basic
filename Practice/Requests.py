import requests
import json

result = requests.get("https://swapi.dev/api/people/3/")
if result.status_code == 200:
    json_dict = json.loads(result.text)
    json_dict['name'] = input("Введите имя: ")
    with open("swap.json", "w") as file:
        json.dump(json_dict, file, indent=4)

    # Доп:
    result_homeworld = requests.get(json_dict['homeworld'])
    print(result_homeworld.text)


# print(swapi.get_film(1))
# Сейчас библиотека не работает, получить начало сюжета можно напрямую

result = requests.get("https://swapi.dev/api/films/1/")

json_dict = json.loads(result.text)

print(json_dict["opening_crawl"])
