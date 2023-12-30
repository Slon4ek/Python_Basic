while True:
    ip_address = input('Введите IP: ')
    if ',' in ip_address:
        print(f'Адрес — это четыре числа, разделённые точками')
        continue

    ip_address = ip_address.split('.')

    for num in ip_address:
        if not num.isnumeric():
            print(f'{num} — это не целое число')
            ip_address = 0
            break
        elif int(num) > 255:
            print(f'{num} превышает 255')
            ip_address = 0
            break
    if ip_address:
        print('IP-адрес корректен')
        break

