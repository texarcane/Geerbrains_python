"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

ln_count = 0
wrd_count = 0

with open("count_file.txt") as count_file:
    for ln in count_file:
        ln_count += 1
        wrd_count += len(ln.split())
        print(f'Number of words in line {ln_count}: {len(ln.split())}')

print(f'\n Total number of lines in file: {ln_count}')
print(f' Total number of words in file : {wrd_count}')
