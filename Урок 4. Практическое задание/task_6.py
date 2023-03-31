"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

source_list = []

a1 = int(input('Enter starting integer of sequence: '))
a2 = int(input('Enter last integer of sequence: '))

print(f'\n Sequence 1:')
for n in count(a1):
    if n > a2:
        break
    else:
        print(n)
        source_list.append(n)

print(f'\n List generated from Sequence 1: {source_list} \n Sequence 2 from generated list:')


b = 0
for n in cycle(source_list):
    if b >= len(source_list):
        break
    print(n)
    b += 1
