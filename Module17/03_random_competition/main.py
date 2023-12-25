import random


def max_score(list_1, list_2, index):
    return max(list_1[index], list_2[index])


team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max_score(team_1, team_2, i_team) for i_team in range(20)]

print(f'Первая команда: {team_1}\n'
      f'Вторая команда: {team_2}\n'
      f'Победители тура: {winners}')
