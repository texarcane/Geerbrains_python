"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

number = float(input('First day result, km: '))
finish = float(input('Desired result per day, km: '))
gains = float(input('Daily distance gain, %: '))
day = 1
while number < finish:
    print(f'{day} day: {number:1.2f} km')
    number = round(number*(1+gains/100), 2)
    day += 1
print(f'{day} day: {number:1.2f} km  \nAnswer: Result of {finish:1.2f} km per day would be achieved on {day} day.')
