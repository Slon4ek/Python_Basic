invalid_chr = ('@', '№', '$', '%', '^', '&', '*', '()')
file_extension = ('.txt', '.docx')
user_input = input('Название файла: ')

if user_input.startswith(invalid_chr):
    print('Ошибка: название начинается недопустимым символом.')
elif not user_input.endswith(file_extension):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно')
