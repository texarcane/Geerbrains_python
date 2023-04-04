"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


academics_dict = dict()
academics_file = open('academics.txt', encoding='utf8')
for ln in academics_file:
    academics_list = ln.split(':')
    academic_hours = 0
    academics_list1 = academics_list[1].split(' ')
    for n in academics_list1:
        if n != '':
            try:
                academic_hours += int(''.join(n1 for n1 in n if n1.isdecimal()))
            except ValueError:
                continue
    academics_dict.update({academics_list[0]: academic_hours})

academics_file.close()
print(academics_dict.copy())
