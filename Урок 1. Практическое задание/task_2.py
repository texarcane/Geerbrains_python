"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

sectime = int(input('Greetings! To convert time into hh:mm:ss format, please enter time in seconds: '))
hours = sectime//3600
minutes = (sectime-hours*3600)//60
seconds = sectime-hours*3600-minutes*60
print(f'The time is {hours:02d}:{minutes:02d}:{seconds:02d}')
