import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result = re.match(r'wo', text)
print("Поиск шаблона в начале строки: ", result)

result = re.search("wo", text)
print("Поиск первого найденного совпадения по шаблону: ", result)

result = re.search("wo", text)
print("Содержимое найденной подстроки: ", result.group(0))

print("Начальная позиция:", result.start())
print("Конечная позиция:", result.end())

result = re.findall("wo", text)
print("Список всех упоминаний шаблона:", result)

result = re.sub("wo", "ЗАМЕНА", text)
print("Текст после замены:", result)

text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
print(re.findall(r'\\wwood\+\?,', text))

text = "Even if they are djinns, I will get djinns that can outdjinn them."
result_1 = re.findall(r"\b[aAeEiIoOuUyY]\w*", text)
print("Слова на гласную:", result_1)
result_2 = re.findall(r"\b[^aAeEiIoOuUyY\W]\w*", text)
print("Слова на любой символ, кроме гласной:", result_2)

text = "Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"

result = re.findall(r"\d{2}-\d{2}-\d{4}", text)

print(result)
