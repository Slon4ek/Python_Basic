import os


def str_count(path: str) -> str:
    line_counter = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                path_to_file = os.path.join(root + '\\' + file)
                with open(path_to_file, 'r', encoding='utf-8') as python_file:
                    for line in python_file:
                        if line.rstrip() and '#' not in line:
                            line_counter += 1
                    yield ''.join('В файле {file_name} - {str_count} строк'.format(
                        file_name=path_to_file, str_count=line_counter
                        )
                    )
                    line_counter = 0


work_dir = os.path.abspath(os.path.join(os.sep, 'SkillBox Python', 'Python_Basic'))
for i in str_count(work_dir):
    print(i)
