import re

phone_list = ['9999999999', '999999-999', '99999x9999']

for num in phone_list:
    if re.fullmatch(r'[89]\d{9}', num):
        print(f'{num}: Номер в порядке')
    else:
        print(f'{num}: Номер не подходит')
