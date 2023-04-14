"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self):
        pass

    @classmethod
    def date_f(cls, date):
        d_list = date.split('.')
        day = int(d_list[0])
        month = int(d_list[1])
        year = int(d_list[2])
        return print(f'Day: {day}, Month: {month}, Year: {year}')

    @staticmethod
    def date_f2(date):
        d_list = date.split('.')

        if int(d_list[0]) > 31 or int(d_list[1]) > 12 or int(d_list[2]) > 2023:
            return print('Error! Date is not valid!')
        else:
            return print('Date is valid')


Date.date_f('01.01.2023')
Date.date_f('31.12.2023')
Date.date_f2('32.10.2023')
Date.date_f2('31.10.2023')
