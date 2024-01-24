class Student:
    def __init__(self, fio, group, score_list):
        self.fio = fio
        self.group = group
        self.score_list = score_list
        self.average_score = sum(score_list) / len(score_list)

    def __str__(self):
        return '{:^40}{:^8}{:^8}'.format(self.fio, self.group, self.average_score)


def sort_key(s):
    return s.average_score


students_list = []
with open('students.txt', 'r', encoding='utf-8') as file:
    for i_line in file:
        i_fio, i_group, i_score_list = i_line.rstrip().split(' : ')
        students_list.append(
            Student(
                fio=i_fio, group=i_group, score_list=[int(score) for score in i_score_list.split()]
            )
        )

sorted_s_list = sorted(students_list, key=sort_key)
for student in sorted_s_list:
    print(student)
