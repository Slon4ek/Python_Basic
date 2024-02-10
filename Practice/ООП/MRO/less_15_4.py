from typing import TextIO


class File:

    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> TextIO:
        self.file = open(self.filename, self.mode, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


class Example:

    def __init__(self):
        print("Вызов __init__")

    def __enter__(self):
        print("Вызов __enter__")
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вызов __exit__")
        if exc_type:
            print(f'Тип ошибки: {exc_type}\nЗначение ошибки: {exc_val}\n"След" ошибки: {exc_tb}')
        return True  # первый вариант без этой строки, второй с этой строкой


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')
