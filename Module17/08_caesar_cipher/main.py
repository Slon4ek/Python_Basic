def encryption(txt, shift):
    letter_list = [(alphabet[(alphabet.index(letter) + shift) % 33]
                   if letter != ' '
                   else ' ')
                   for letter in txt]
    encryption_txt = ''
    for i_let in letter_list:
        encryption_txt += i_let
    return encryption_txt


alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
alphabet.insert(6, 'ё')

user_txt = input('Введите сообщение: ')
user_shift = int(input('Введите сдвиг: '))
print(encryption(user_txt, user_shift))
