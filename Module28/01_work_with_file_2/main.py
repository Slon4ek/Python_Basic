from typing import TextIO


class File:

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> TextIO:
        try:
            self.file = open(self.filename, self.mode, encoding='utf8')
        except FileNotFoundError:
            self.file = open(self.filename, 'x', encoding='utf-8')
            self.__enter__()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type:
            return True
        self.file.close()


with File('asd.txt', 'w') as file:
    file.write('asd')
