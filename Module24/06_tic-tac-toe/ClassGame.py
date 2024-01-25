from ClassBoard import Board
from ClassPlayer import Player


class Game:

    def __init__(self, name_1, name_2):
        self.game_status = True
        self.board = Board()
        self.player_x = Player(name_1)
        self.player_0 = Player(name_2)

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
        while self.game_status:
            print('Ход игрока {}'.format(self.player_x.name))
            step = self.player_move(self.player_x, 'X')
            if step:
                self.board.print_board()
            if self.board.is_full():
                print('Игра окончена.', end=' ')
                self.start_new_game()
                break
            print('Ход игрока {}'.format(self.player_0.name))
            step = self.player_move(self.player_0, '0')
            if step:
                self.board.print_board()

    def start_new_game(self):
        while self.game_status:
            answer = input('Хотите продолжить играть? 1 - Да, 2 - Нет: ')
            if answer == '1':
                self.start_game()
            elif answer == '2':
                self.game_status = False
            else:
                print('Ошибка ввода!')
