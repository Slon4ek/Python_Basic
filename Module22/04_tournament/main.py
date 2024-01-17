def open_file(file_name):
    # Открываем файл, считываем первые 2 символа и записываем в переменную passing_score -
    # количество очков для прохода во второй тур. Переводим курсор на 4 позицию и считываем табицу
    # участников
    file = open(file_name, 'r')
    passing_score = file.read(2)
    file.seek(4)
    players_list = file.read().split('\n')
    file.close()
    return players_list, passing_score


def write_file(lst):
    # Записываем в файл информацию об участниках, которые прошли во второй тур
    file = open('second_tour.txt', 'w')
    file.write(str(len(lst)) + '\n')
    for i_line in lst:
        file.write(i_line + '\n')
    file.close()


p_comp, pass_score = open_file('first_tour.txt')
new_players_list = []

for line in p_comp:
    surname, name, score = line.split()
    player_info = ''.join('{}. {} {}'.format(name[0], surname, score))
    if int(score) > int(pass_score):
        new_players_list.append(player_info)

write_file(new_players_list)
