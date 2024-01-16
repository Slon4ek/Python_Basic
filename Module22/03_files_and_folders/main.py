import os


def dir_info(path_to_dir):
    dir_count = 0
    file_count = 0
    files_size = 0
    for obj in os.listdir(path_to_dir):
        path = os.path.abspath(os.path.join(path_to_dir, obj))
        if os.path.isfile(path):
            files_size += os.path.getsize(path)
            file_count += 1
        elif os.path.isdir(path):
            dir_count += 1
            dc, fc, fs = dir_info(path)
            dir_count += dc
            file_count += fc
            files_size += fs
    return dir_count, file_count, files_size


work_dir = os.path.abspath(os.path.join(os.sep, 'SkillBox Python'))
if os.path.exists(work_dir):
    dir_quantity, file_quantity, dir_size = dir_info(work_dir)
    print(f'Размер каталога (в Кбайтах): {dir_size / 1024}\n'
          f'Количество подкаталогов: {dir_quantity}\n'
          f'Количество файлов: {file_quantity}')
else:
    print('Такого каталога не существует!')
