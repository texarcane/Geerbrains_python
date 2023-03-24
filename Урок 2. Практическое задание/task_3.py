"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month_inp = int(input('Hello! Please enter months number: '))
sn_list = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn',
           'Autumn', 'Winter']

sn_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
           9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

if month_inp < 1 or month_inp > 12:
    print('Invalid months number!')
else:
    print(f'List result: {sn_list[month_inp - 1]}')
    print(f'Dictionary result: {sn_dict[month_inp]}')
