"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

ln_count = 0
total_salary = 0
salary_list = []
salary_file = open("salaries.txt", encoding="utf8")
for ln in salary_file:
    ln_count += 1
    salary_list = ln.split()
    total_salary = total_salary + float(salary_list[1])
    if float(salary_list[1]) < 20000:
        print(f"{salary_list[0]}'s salary is lower than 20000. {salary_list[0]}'s salary: {salary_list[1]}")
salary_file.close()
print(f' \n Average salary: {total_salary / ln_count:.2f}')
