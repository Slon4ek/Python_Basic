from ClassGame import Game

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
new_game = Game(player_1, player_2)
new_game.start_game()
