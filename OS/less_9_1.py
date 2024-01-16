import os


def print_dirs(proj):
    print('\nСодержимое дирректории', proj)
    for elem in os.listdir(proj):
        path = os.path.join(proj, elem)
        print('   ', path)


file_name = 'admin.bat'
folder_name = 'access'
relative_path = os.path.join('../..', folder_name, file_name)
abs_path = os.path.abspath(os.path.join(file_name))
print(relative_path)
print(abs_path)

projects_list = ['Projects', 'Python_basic']
for project in projects_list:
    path_to_project = os.path.abspath(os.path.join('../..', project))
    print_dirs(path_to_project)


print("Корень диска:", os.path.abspath(os.sep))