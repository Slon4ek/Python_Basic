import os


def find_obj(cur_path, ending):
    """Функция поиска файла"""
    paths_list = []
    for elem in os.listdir(cur_path):
        path = os.path.join(cur_path, elem)
        if elem.endswith(ending):
            paths_list.append(path)
        if os.path.isdir(path):
            result = find_obj(path, ending)
            if result:
                paths_list.extend(result)
    return paths_list


def get_text_from_file(path_to_file):
    file = open(path_to_file, 'r', encoding='utf-8')
    text = file.name + '\n\n'
    for line in file:
        text += line
    file.close()
    return text


work_dir = os.path.abspath(os.path.join(os.sep, 'SkillBox Python', 'Python_Basic'))

find_objects = find_obj(work_dir, '.py')
write_file = open('scripts.txt', 'w', encoding='utf-8')
for path in find_objects:
    write_file.write(get_text_from_file(path) + '\n'*2 + '*'*80 + '\n'*2)
write_file.close()
