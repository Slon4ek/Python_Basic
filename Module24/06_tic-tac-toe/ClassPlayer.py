class Player:
    def __init__(self, name):
        self.name = name
        self.win_count = 0

    def make_a_move(self):
        cell_num = input('Введите номер клетки: ')
        try:
            cell_num = int(cell_num)
        except ValueError:
            print('Неверный ввод! Введите число от 1 до 9')
            return self.make_a_move()
        if cell_num < 0 or cell_num > 9:
            print('Неверный номер клетки! Введите число от 1 до 9')
            return self.make_a_move()
        return cell_num

