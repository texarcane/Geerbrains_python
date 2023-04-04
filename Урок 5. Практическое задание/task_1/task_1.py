"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

out_f = open('output_file.txt', 'w')

input_txt = " "
while input_txt != '':
    input_txt = input('Enter string to be written in the file: ')
    if input_txt == '':
        break
    else:
        out_f.write(input_txt)
        out_f.write("\n")
out_f.close()
