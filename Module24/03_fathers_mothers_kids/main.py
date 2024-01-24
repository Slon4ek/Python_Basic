from Classes import Parent

father = Parent('Федор', 39)
father.add_kid('Ваня', 13)
father.add_kid('Вероника', 17)
father.print_info()
print(father.kids_list)
for kid in father.kids_list:
    kid.print_state()
    father.feed(kid.name)
    father.calm(kid.name)
