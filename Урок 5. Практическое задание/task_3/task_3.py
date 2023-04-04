"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

numbers_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
number_file = open("numbers.txt", encoding="utf8")
number_file_new = open("numbers_new.txt", "w")
number_list = []

for ln in number_file:
    number_list = ln.split()
    number_list[0] = numbers_dict.get(number_list[0])
    number_file_new.write(" ".join(number_list))
    number_file_new.write("\n")

number_file.close()
number_file_new.close()
