'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

with open('for_task7.txt', 'r', encoding='utf-8') as f:
    list_of_companies = []
    for line in f:
        list_of_companies.append(line)

for i in range(len(list_of_companies)):
    list_of_companies[i] = list_of_companies[i].split()

sum_of_profit = 0
count = 0

for i in range(len(list_of_companies)):
    list_of_companies[i].pop(1)
    for j in range(1, len(list_of_companies[i])):
        list_of_companies[i][j] = int(list_of_companies[i][j])
    profit = list_of_companies[i][1] - list_of_companies[i][2]
    list_of_companies[i].append(profit)
    while len(list_of_companies[i]) > 2:
        list_of_companies[i].pop(1)
    if list_of_companies[i][1] > 0:
        sum_of_profit += list_of_companies[i][1]
        count += 1

average = sum_of_profit / count
dict_of_average = {'average_profit': average}
dict_of_companies = dict(list_of_companies)
result_list = [dict_of_companies, dict_of_average]

with open('companies_from_task7.json', 'w', encoding='utf-8') as write_to_json:
    json.dump(result_list, write_to_json)
