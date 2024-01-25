from ClassBoard import Board
from ClassPlayer import Player


class Game:
    win_combinations = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    def __init__(self, name_1, name_2):
        self.game_status = True
        self.board = Board()
        self.player_x = Player(name_1, 'X')
        self.player_0 = Player(name_2, '0')

    def player_move(self, player, sym):
        cell_num = player.make_a_move()
        result = self.board.change_cell_status(cell_num, sym)
        if result:
            return True
        else:
            print('Клетка занята!')
            self.player_move(player, sym)

    def start_game(self):
        self.board = Board()
        for i in range(9):
            if i % 2 == 0:
                player = self.player_x
            else:
                player = self.player_0
            print('Ход игрока {}'.format(player.name))
            step = self.player_move(player, player.sym)
            if step:
                self.board.print_board()
                result = self.check_winner()
                if result:
                    self.end_round()
                    break

    def end_round(self):
        print('Раунд завершен.', end=' ')
        self.start_new_game()

    def start_new_game(self):
        print('Статистика игроков:\n\t{} : {} побед\n\t{} : {} побед'.format(
            self.player_x.name, self.player_x.win_count,
            self.player_0.name, self.player_0.win_count
        ))
        while self.game_status:
            answer = input('Хотите продолжить играть? 1 - Да, 2 - Нет: ')
            if answer == '1':
                self.start_game()
            elif answer == '2':
                self.game_status = False
            else:
                print('Ошибка ввода!')

    def check_winner(self):
        for combination in self.win_combinations:
            if all([True if self.board.cells[i].sym == 'X' else False for i in combination]):
                self.player_x.win_count += 1
                print('Выиграл игрок {}'.format(self.player_x.name))
                return True
            elif all([True if self.board.cells[i].sym == '0' else False for i in combination]):
                self.player_0.win_count += 1
                print('Выиграл игрок {}'.format(self.player_0.name))
                return True
        return False
