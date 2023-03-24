"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

i_name = 'Enter items name: '
i_price = 'Enter items price: '
i_qn = 'Enter items quantity: '
i_unit = 'Enter items units: '
i_k1 = 'name'
i_k2 = 'price'
i_k3 = 'quantity'
i_k4 = 'units'
end = ''
num = 1
list_1 = []
while end != 'Stop':
    dict_1 = {i_k1: input(i_name), i_k2: input(i_price), i_k3: input(i_qn), i_k4: input(i_unit)}
    tup_1 = (num, dict_1)
    list_1.append(tup_1)
    num += 1
    end = input('To end the list enter "Stop". To continue enter any letter.')
    if end == "Stop":
        break
print("Current storage list: ")
print(*list_1, sep='\n')

nm_list = []
pr_list = []
qn_list = []
un_list = []
store_dict = {'item_names': nm_list, 'prices': pr_list, 'quantity': qn_list, 'units': un_list}
for item in list_1:
    for value in item:
        if type(value) is dict:
            nm_list.append(value['name'])
            pr_list.append(value['price'])
            qn_list.append(value['quantity'])
            un_list.append(value['units'])
print("Storage analytics: ")
for key, value in store_dict.items():
    print(key, ':', value)
