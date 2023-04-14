"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class WrongValue(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
while True:
    try:
        n = input('Enter number to proceed or "q" to finish:')
        if n == 'q':
            break
        elif n.isdigit():
            num_list.append(int(n))
        else:
            raise WrongValue('Not a number!')
    except WrongValue as w:
        print(w.txt)

print(num_list)
