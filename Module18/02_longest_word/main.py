input_str = input('Введите строку: ').split(' ')

max_len = max(len(word) for word in input_str)
max_word = ''

for word in input_str:
    if len(word) == max_len:
        max_word = word
        break

if max_len == 1:
    ending = ''
elif 1 < max_len < 5:
    ending = 'а'
else:
    ending = 'ов'

print(f'Самое длинное слово: {max_word}\n'
      f'Длина этого слова: {max_len} символ{ending}')
