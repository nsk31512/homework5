'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

with open('for_task2.txt', 'r', encoding='utf-8') as poem:
    count_lines = 0
    count_words = 0
    for line in poem:
        count_lines += 1
        list_of_words = str(line).split()
        for item in list_of_words:
            if item == '-':
                list_of_words.remove(item)
        print(f'В {count_lines} строке {len(list_of_words)} слов(а)')

print(f'Всего строк в файле: {count_lines}')
