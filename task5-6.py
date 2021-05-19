'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
 Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

with open('for_task6.txt', 'r', encoding='utf-8') as f:
    list_of_disciplines = []
    for line in f:
        list_of_disciplines.append(line)

for i in range(len(list_of_disciplines)):
    list_of_disciplines[i] = list_of_disciplines[i].split()

for i in range(len(list_of_disciplines)):
    sum = 0
    for j in range(1, len(list_of_disciplines[i])):
        if list_of_disciplines[i][j] != '-':
            index_of_bracket = list_of_disciplines[i][j].index('(')
            list_of_disciplines[i][j] = int(list_of_disciplines[i][j][:index_of_bracket])
            sum += list_of_disciplines[i][j]
    list_of_disciplines[i].append(sum)
    while len(list_of_disciplines[i]) > 2:
        list_of_disciplines[i].pop(1)

print(dict(list_of_disciplines))
