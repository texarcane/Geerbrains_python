"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv


def wage_w(hours, rate, bonuses):
    return round(float(hours) * float(rate) + float(bonuses), 2)


try:
    script_name, work_hours, rph, bonus = argv
except ValueError:
    print('ERROR! Wrong value!')
    exit()
wage = wage_w(work_hours, rph, bonus)

print(f'\n Working hours: {work_hours} \n Rate per hour: {rph} \n Bonus: {bonus} \n  \n Your Wage: {wage}')
