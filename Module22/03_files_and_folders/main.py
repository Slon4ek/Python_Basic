import os


def output(folder_size_bytes, subfolders_qty, files_qty):
    print("Размер каталога (в Кб): {:.04f}".format(folder_size_bytes / 1024))
    print("Количество подкаталогов:", subfolders_qty)
    print("Количество файлов:", files_qty)


folder_path = os.path.abspath(os.path.join(os.sep, 'SkillBox Python'))
files_lst = []
subdirs = []
for root, dirs, files in os.walk(folder_path):
    for name in files:
        files_lst.append(os.path.join(root, name))
    for name in dirs:
        subdirs.append(os.path.join(root, name))

folder_size_bytes = 0
for file_name in files_lst:
    folder_size_bytes += os.path.getsize(file_name)

output(folder_size_bytes, len(subdirs), len(files_lst))
