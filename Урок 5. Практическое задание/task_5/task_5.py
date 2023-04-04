"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


number_file = open('sum_numbers.txt', 'w+')
number_file.write(input('Enter integers divided by spaces: '))
number_file.seek(0)
numbers = number_file.readline()
number_list = numbers.split()
result = 0

for n in number_list:
    print(n)
    result += int(n)

number_file.close()
print(f'\n Sum of all numbers in file is {result}')
