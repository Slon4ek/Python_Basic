import random


def vicious_cycle(file_name):
    sum_numbers = 0
    while sum_numbers < 777:
        try:
            user_num = int(input('Введите число: '))
            random_num = random.randint(1, 13)
            if random_num == 5:
                raise TypeError()
            file_name.write(str(user_num) + '\n')
            sum_numbers += user_num
        except ValueError:
            print('Вы ввели что-то не похожее на число:(')
        except TypeError:
            print('Вас постигла неудача!')
            sum_numbers = 0
            break

    return sum_numbers


with open('out_file.txt', 'a') as file:
    if vicious_cycle(file):
        print('Вы успешно выполнили условие для выхода из порочного цикла!')

with open('out_file.txt', 'r') as read_file:
    print('Содержимое файла out_file.txt: \n'
          '{}'.format(read_file.read()))
