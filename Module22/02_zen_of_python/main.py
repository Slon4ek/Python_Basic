def invert_output(file_name):
    # Функция печатает текст из файла снизу вверх
    file = open(file_name, 'r')
    lines_list = [line for line in file]
    for line in lines_list[::-1]:
        print(line, end='')
    file.close()


invert_output('zen.txt')
