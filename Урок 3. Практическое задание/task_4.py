"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    answer = 1
    for a in range(abs(y)):
        answer *= x
    if y >= 0:
        return print('ERROR! This is not negative integer!')
    elif x <= 0:
        return print('ERROR! This is not positive real number!')
    else:
        return 1 / answer


print(my_func(float(input('Enter positive real number: ')), int(input('Enter negative integer: '))))
