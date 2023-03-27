"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def division(n1, n2):

    try:
        print(float(n1) / float(n2))
    except ZeroDivisionError:
        print('Cant divide by zero!')
    except TypeError:
        print('Wrong data type!')
    except ValueError:
        print('Wrong data!')


division(n1=input('First number: '), n2=input('Second number: '))
