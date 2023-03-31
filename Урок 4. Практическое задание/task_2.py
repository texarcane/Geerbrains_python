"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""


source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(f'Source list: \n {source_list}')

res_list = [source_list[n] for n in range(1, len(source_list)) if source_list[n] > source_list[n-1]]

print(f'Resulting list with generator: \n {res_list}')

res_no_gen_list = []
for n in range(1, len(source_list)):
    if source_list[n] > source_list[n - 1]:
        res_no_gen_list.append(int(source_list[n]))

print(f'Resulting list with no generator: \n {res_no_gen_list}')
