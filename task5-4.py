'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
'''

dict_for_file = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }

with open('for_task4.txt', 'r', encoding='utf-8') as origin_f:
    list_of_origin_txt = []
    for line in origin_f:
        list_of_origin_txt.append(line.split())

for el in list_of_origin_txt:
    for i in range(len(el)-1):
        for key, value in dict_for_file.items():
            if key == el[i]:
                el[i] = value

new_list_of_txt = []
for item in list_of_origin_txt:
    new_list_of_txt.append(' '.join(item))

with open('result_of_task4.txt', 'w', encoding='utf-8')as result_f:
    result_f.write('\n'.join(new_list_of_txt))
