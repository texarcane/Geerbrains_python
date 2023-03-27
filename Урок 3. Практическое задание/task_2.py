"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_data(name, surname, birth_year, city, email, phone):
    return f'{name} {surname} was born in {birth_year} and lives in {city}, his email: {email}, his number: {phone}'


print(user_data(name=input('Name: '), surname=input('Surname: '), birth_year=input('Birthday year: '),
                city=input('City: '), email=input('Email: '), phone=input('Phone: ')))
