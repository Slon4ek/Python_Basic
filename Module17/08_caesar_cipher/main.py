def encryption(txt, shift):
    letter_list = [(alphabet[(alphabet.index(letter) + shift) % 33]
                   if letter != ' '
                   else ' ')
                   for letter in txt]
    encryption_txt = ''.join(letter_list)
    return encryption_txt


alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
alphabet.insert(6, 'ё')

user_txt = input('Введите сообщение: ').lower()
user_shift = int(input('Введите сдвиг: '))
print(f'Зашифрованное сообщение: "{encryption(user_txt, user_shift)}"')
