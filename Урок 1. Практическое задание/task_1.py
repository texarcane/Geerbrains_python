"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

nameinput = input('Greetings! Enter your name and surname: ')
monthsinput = int(input('Please enter period in months: '))
salaryinput = float(input('Please enter salary sum: '))
avgsalary = round(salaryinput/monthsinput, 2)
print(f'{nameinput} has earned {avgsalary} dollars in average for {monthsinput} months.')
