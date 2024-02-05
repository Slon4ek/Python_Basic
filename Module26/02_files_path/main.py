import os


def gen_files_path(directory: str, path: str = os.path.abspath(os.sep)) -> str:
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            if dir_name == directory:
                for file in files:
                    path_to_file = os.path.join('{}\\{}\\{}'.format(root, dir_name, file))
                    yield path_to_file


for files_path in gen_files_path('Python_Basic'):
    print(files_path)
