user_word = input('Введите слово: ')
user_word = user_word.lower()
revers_word = user_word[::-1]

if user_word == revers_word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')