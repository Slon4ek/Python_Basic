def count_uppercase_lowercase(txt):
    upper = [sym for sym in txt if sym.isupper()]
    lower = [sym for sym in txt if sym.islower()]
    return len(upper), len(lower)


# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
