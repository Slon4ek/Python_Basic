vowel_in_text = [vow for vow in input('Введите текст: ') if vow.lower() in 'аеёиоуыэюя']

print(f'Список гласных букв: {vowel_in_text}\n'
      f'Длина списка: {len(vowel_in_text)}')
