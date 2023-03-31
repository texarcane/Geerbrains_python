"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""

from functools import reduce

source_list = [n for n in range(100, 1001, 2)]

print(f'Source list: \n {source_list}')

result = reduce(lambda a, b: a * b, source_list)

print(f'Result: \n {result}')
