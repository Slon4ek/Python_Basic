from Classes import Parent

father = Parent('Федор', 39)
father.add_kid('Ваня', 13)
father.add_kid('Вероника', 17)
father.print_info()
print(father.kids_list)
for kid in father.kids_list:
    if not kid.is_full() and not kid.is_calm():
        kid.print_state()
        father.feed(kid.name)
        father.calm(kid.name)
        print('Ребенок покормлен и успокоен')

for kid in father.kids_list:
    kid.print_state()
