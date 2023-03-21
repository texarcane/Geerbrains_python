"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num = int(input('Greetings! Give me positive integer n: \n'))
n = int("%s" % num)
nn = int("%s%s" % (num, num))
nnn = int("%s%s%s" % (num, num, num))
n_sum = int(n+nn+nnn)
print(f'Sum of n+nn+nnn is {n}+{nn}+{nnn} = {n_sum}')
