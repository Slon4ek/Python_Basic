students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def students_interest(dictionary):
    stud_interest = [interest
                     for student in dictionary.values()
                     for interest in student['interests']
                     ]
    surname_len = ''
    for student in dictionary.values():
        surname_len += ''.join(student['surname'])
    return stud_interest, surname_len


id_age = [(id_num, student['age']) for id_num, student in students.items()]
print(f'Список пар «ID студента — возраст»: {id_age}')

interest_list, all_surname = students_interest(students)

print(f'Полный список интересов всех студентов: {interest_list}\n'
      f'Общая длина всех фамилий студентов: {len(all_surname)}')
