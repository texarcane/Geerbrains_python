"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


numerator = int(input('Enter numerator: '))
denominator = int(input('Enter denominator: '))

try:
    if denominator == 0:
        raise ZeroDivision('Dividing by zero!')
    else:
        result = numerator / denominator
except ZeroDivision as err:
    print(err)
else:
    print(f'Result: {numerator} / {denominator} = {result}')
