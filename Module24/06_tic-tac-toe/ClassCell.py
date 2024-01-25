class Cell:
    def __init__(self, num, sym=' '):
        self.empty_status = True
        self.num = num
        self.sym = sym

    def __format__(self, format_spec):
        return self.sym

