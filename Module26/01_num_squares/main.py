class SquaresOfNumbers:
    def __init__(self, n: int) -> None:
        self.end = n
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        return self.start ** 2


def square(n) -> int:
    start_num = 1
    for num in range(n):
        yield start_num ** 2
        start_num += 1


user_num = int(input('Введите число: '))
squares = (num ** 2 for num in range(1, user_num + 1))
for num in squares:
    print(num)
