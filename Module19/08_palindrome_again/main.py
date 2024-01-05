def palindrome(string):
    sym_dict = {
        sym: string.count(sym)
        for sym in string
    }
    odd_count = 0
    for val in sym_dict.values():
        if int(val) % 2 != 0:
            odd_count += 1
    if odd_count > 1:
        print('Нельзя сделать палиндромом')
    else:
        print('Можно сделать палиндромом')


user_str = input('Введите строку: ')
palindrome(user_str)
