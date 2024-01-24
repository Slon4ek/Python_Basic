import os
work_file_1 = os.path.abspath(os.path.join(os.sep, 'Task', 'Additional_info', 'group_1.txt'))
work_file_2 = os.path.abspath(os.path.join(os.sep, 'Task', 'Additional_info', 'group_2.txt'))

file = open(work_file_1, 'r', encoding='utf8')
summ = 0
diff = 0
compose = 1
for line in file:
    info = line.split()
    summ += int(info[2])
    diff -= int(info[2])
print(f'Сумма очков первой группы: {summ}\n'
      f'Разность очков первой группы: {diff}')
file.close()
file = open(work_file_2, 'r', encoding='utf8')
for line in file:
    info = line.split()
    compose *= int(info[2])
print(f'Произведение очков второй группы: {compose}')
file.close()

