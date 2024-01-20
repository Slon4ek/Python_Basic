def validator(line):
    try:
        line_list = line.split()
        name, email, age = line_list[0], line_list[1], line_list[2]
        if not name.isalpha():
            raise NameError
        if '@' not in email and '.' not in email:
            raise SyntaxError
        if int(age) < 10 or int(age) > 99:
            raise ValueError
    except IndexError:
        error_str = ''.join('НЕ присутствуют все три поля: IndexError')
        return error_str
    except NameError:
        error_str = ''.join('Поле «Имя» содержит НЕ только буквы: NameError')
        return error_str
    except SyntaxError:
        error_str = ''.join('Поле «Имейл» НЕ содержит @ и точку: SyntaxError')
        return error_str
    except ValueError as exc:
        error_str = ''.join('Поле «Возраст» НЕ представляет число от 10 до 99: ValueError')
        return error_str
    else:
        return True


with open('registrations.txt', 'r', encoding='utf-8') as reg_file, \
        open('registrations_good.log', 'w', encoding='utf-8') as good, \
        open('registrations_bad.log', 'w', encoding='utf-8') as bad:
    for i_line in reg_file:
        clear_line = i_line.rstrip()
        result = validator(clear_line)
        if isinstance(result, str):
            bad.write(''.join('>>{: <40}>>>{: <40}\n'.format(clear_line, result)))
        else:
            u_name, e_mail, u_age = clear_line.split()
            good.write(''.join('{: <15}{: <25}{: <3}\n'.format(u_name, e_mail, u_age)))
