class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = []

    def __str__(self):
        result = ''
        for i_row in range(self.row):
            for i, num in enumerate(self.data[i_row]):
                result += ''.join('{: ^3}'.format(str(num)))
            result += '\n'
        return result

    def add(self, other):
        result = Matrix(self.row, self.col)
        try:
            result.data = [
                [self.data[i_row][i_col] + other.data[i_row][i_col]
                 for i_col in range(self.col)]
                for i_row in range(self.row)
            ]
        except IndexError:
            print('Операция сложения применима только к матрицам одинакового размера!')
            return None
        return result

    def subtract(self, other):
        result = Matrix(self.row, self.col)
        try:
            result.data = [
                [self.data[i_row][i_col] - other.data[i_row][i_col]
                 for i_col in range(self.col)]
                for i_row in range(self.row)
            ]
        except IndexError:
            print('Операция вычитание применима только к матрицам одинакового размера!')
            return None
        return result

    def multiply(self, other):
        result = Matrix(self.row, other.col)
        result.data = [
            [None for _ in range(other.col)] for _ in range(self.row)
        ]
        for i in range(self.row):
            for j in range(other.col):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(other.row))
        return result

    def transpose(self):
        result = Matrix(self.col, self.row)
        result.data = [
            [self.data[i][j] for i in range(self.row)] for j in range(self.col)
        ]
        return result


# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
