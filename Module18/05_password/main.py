while True:
    user_pass = input('Придумайте пароль: ')
    if len([letter for letter in user_pass if letter.isupper()]) < 1\
            or len([digit for digit in user_pass if digit.isdigit()]) < 3\
            or len(user_pass) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль.')
        break
