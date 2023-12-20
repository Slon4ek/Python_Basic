vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
user_input = input('Введите текст: ')
vowel_in_text = [vow for vow in user_input if vow in vowel_letters]

print(f'Список гласных букв: {vowel_in_text}\n'
      f'Длина списка: {len(vowel_in_text)}')
