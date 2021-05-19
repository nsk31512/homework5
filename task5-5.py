'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

with open('for_task5.txt', 'r', encoding='utf-8') as f:
    str_of_numbers = f.readline()
    list_of_numbers = str_of_numbers.split()

for i in range(len(list_of_numbers)):
    list_of_numbers[i] = int(list_of_numbers[i])
summator = 0
for item in list_of_numbers:
    summator += item
print(summator)
