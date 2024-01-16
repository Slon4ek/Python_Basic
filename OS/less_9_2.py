import os
import random


def find_obj(cur_path, obj_name):
    """Функция поиска файла"""
    paths_list = []
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if obj_name == elem:
            paths_list.append(path)
        if os.path.isdir(path):
            result = find_obj(path, obj_name)
            if result:
                paths_list.extend(result)
    return paths_list


find_objects = find_obj(os.path.abspath(os.path.join(os.sep, 'SkillBox Python')), 'README.md')

rand_num = random.randint(1, 10)
file = open(find_objects[rand_num], 'r', encoding='utf-8')
print(file.name)
for line in file:
    print(line, end='')
file.close()
history_file = open('history_search.txt', 'w')
for path in find_objects:
    history_file.write(path)
    history_file.write('\n')
history_file.close()
# object_name = 'less_9_1'
# abs_path = os.path.abspath(os.path.join(object_name))
# if os.path.exists(abs_path):
#     if os.path.isdir(abs_path):
#         print(f'{abs_path} - это папка')
#     elif os.path.isfile(abs_path):
#         print(f'{abs_path} - это файл')
#         print(f'Размер файла: {os.path.getsize(object_name)}')
# else:
#     print('Обьект не найден')
