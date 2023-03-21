"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

num = int(input('Greetings! Enter positive integer: '))
max_number = 0
while num > 0:
    digit = num % 10
    num = num//10
    if digit > max_number:
        max_number = digit
print(f'Largest digit in given number: {max_number}')
