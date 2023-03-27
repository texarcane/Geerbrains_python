"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def my_func():
    result = 0
    stop = False
    while not stop:
        num_input = input('Enter numbers divided by space, to stop enter "s": ').split()
        result1 = 0
        for n in range(len(num_input)):
            try:
                if num_input[n] == 's':
                    stop = True
                else:
                    result1 = result1 + int(num_input[n])
            except ValueError:
                print('ERROR! Wrong value!')
                break
        result = result + result1
        print(f'Current sum of the entered numbers is {result}')
    return f'Resulting sum of the entered numbers is {result}'


print(my_func())
