'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('for_task3.txt', 'r', encoding='utf-8') as file_workers:
    list_of_workers_with_salary_less_20 = []
    sum_of_salary = 0
    count_of_workers = 0
    for line in file_workers:
        count_of_workers += 1
        list_of_line = str(line).split()
        for i in range(len(list_of_line)):
            salary_in_int = int(list_of_line[1])
        sum_of_salary += salary_in_int
        if salary_in_int < 20:
            list_of_workers_with_salary_less_20.append(list_of_line[0])


print(f'Средний оклад сотрудников: {sum_of_salary / count_of_workers: {0}.{4}} тысяч рублей')
print('-' * 10)
for surname in list_of_workers_with_salary_less_20:
    print(f'{surname} имеет оклад менее 20 тысяч рублей')
