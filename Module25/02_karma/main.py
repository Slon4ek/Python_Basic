import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Life:
    __karma = 500

    def __init__(self):
        self.current_karma = 0

    def get_karma(self):
        return self.__karma

    def one_day(self):
        num = random.randint(1, 10)
        exception_num = random.randint(1, 5)
        if num == 5:
            if exception_num == 1:
                raise KillError('Убивать нельзя, карма от этого не увеличивается :(')
            elif exception_num == 2:
                raise DrunkError('Пить нельзя, карма от этого не увеличивается :(')
            elif exception_num == 3:
                raise CarCrashError('Сломалась машина, карма от этого не увеличивается :(')
            elif exception_num == 4:
                raise GluttonyError('Обжираться нельзя, карма от этого не увеличивается :(')
            elif exception_num == 5:
                raise DepressionError('Депрессия, карма от этого не увеличивается :(')
        else:
            return random.randint(1, 7)


life = Life()
with open('karma.log', 'w', encoding='utf-8') as log_file:
    day_count = 0
    while life.current_karma != life.get_karma():
        try:
            life.current_karma += life.one_day()
            print('Прошел очередной день.\n\tКоличество кармы: {}'.format(life.current_karma))
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            log_file.write(str(exc) + '\n')
        day_count += 1
print('Набрано 500 кармы за {} дней'.format(day_count))
