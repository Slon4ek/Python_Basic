import random
nums_list = [
    random.randint(0, 100)
    for _ in range(10)
]
new_list = [
    (val, nums_list[i+1])
    for i, val in enumerate(nums_list)
    if i < 9 and i % 2 == 0
]

print(f'Оригинальный список: {nums_list}\n'
      f'Новый список: {new_list}')
