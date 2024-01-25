from ClassCell import Cell


class Board:
    def __init__(self):
        self.cells = [Cell(num) for num in range(1, 10)]

    def change_cell_status(self, cell_num, sym):
        cell_num -= 1
        if self.cells[cell_num].empty_status:
            self.cells[cell_num].sym = sym
            self.cells[cell_num].empty_status = False
            return True
        else:
            return False

    def is_full(self):
        for i in self.cells:
            if i.empty_status:
                return False
        return True

    def print_board(self):
        print('+---+---+---+')
        print('| {} | {} | {} |'.format(self.cells[0], self.cells[1], self.cells[2]))
        print('+---+---+---+')
        print('| {} | {} | {} |'.format(self.cells[3], self.cells[4], self.cells[5]))
        print('+---+---+---+')
        print('| {} | {} | {} |'.format(self.cells[6], self.cells[7], self.cells[8]))
        print('+---+---+---+')

# board = Board()
# board.is_full()
# board.cells[0].empty_status = False
# board.cells[1].empty_status = False
# board.cells[2].empty_status = False
# board.cells[3].empty_status = False
# board.cells[4].empty_status = False
# board.cells[5].empty_status = False
# board.cells[6].empty_status = False
# board.cells[7].empty_status = False
# board.cells[8].empty_status = True
# board.is_full()