"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num_input = int(input('Greetings! Give me positive integer: \n'))
n = int(num_input)
sum_input = int(n*1+n*11+n*111)
print(f'n+nn+nnn sum is {sum_input}')
