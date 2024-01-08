def is_prime(num):
    divider = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divider += 1
    if num <= 1 or divider != 0:
        return False
    else:
        return True


def crypto(u_list):
    return list(sym for i_sym, sym in enumerate(u_list) if is_prime(i_sym))


print(crypto('О Дивный Новый мир!'))
