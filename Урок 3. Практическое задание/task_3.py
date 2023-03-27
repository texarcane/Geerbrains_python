"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(n1, n2, n3):
    sum_n = [float(n1), float(n2), float(n3)]
    sum_n.sort()
    sum_n.reverse()
    return f' Using sort, sum of two largest numbers is {sum_n[0] + sum_n[1]}'


print(my_func(n1=input('First number: '), n2=input('Second number: '), n3=input('Third number: ')))


def my_func2(n1, n2, n3):
    sum_n = [float(n1), float(n2), float(n3)]
    max1 = max(sum_n)
    sum_n.pop(sum_n.index(max(sum_n)))
    max2 = max(sum_n)
    return f' Without sort, sum of two largest numbers is {max1 + max2}'


print(my_func2(n1=input('First number: '), n2=input('Second number: '), n3=input('Third number: ')))
