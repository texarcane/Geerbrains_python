"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Storage:
    office_dict = {}

    def office_tech(self, equipment):
        if not isinstance(equipment, Equipment):
            raise Exception('Warning!')
        if self.office_dict.get(equipment) is not None:
            self.office_dict[equipment] += 1
        else:
            self.office_dict[equipment] = 1

    def res_dict(self):
        for m, q in self.office_dict.items():
            print(f'{m} : {q} units')


class Equipment:
    def __init__(self, tech: str, brand: str, model: str, price: float):
        self.tech = tech
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f'{self.brand} {self.model}'


class Printer(Equipment):
    def __init__(self, brand: str, model: str, price: float, print_type: str):
        super().__init__('Printer', brand, model, price)
        self.type = print_type


class Scanner(Equipment):
    def __init__(self, brand: str, model: str, price: float, scan_size: str):
        super().__init__('Scanner', brand, model, price)
        self.scan = scan_size


class Copier(Equipment):
    def __init__(self, brand: str, model: str, price: float, resolution: str):
        super().__init__('Xerox', brand, model, price)
        self.res = resolution


printer_1 = Printer('Canon', 'LBP233dw', 17500, 'Laser')
printer_2 = Printer('Epson', 'EcoTank M1100', 14200, 'Inkjet')

scanner_1 = Scanner('Avision', 'FB10', 12599, 'Book')
scanner_2 = Scanner('Plustek', 'OpticFilm 8100', 25500, 'Slide-scanner')

copier_1 = Copier('Canon', 'mageRUNNER 2206', 99990, '600x600')
copier_2 = Copier('Brother', 'T420W', 23000, '1200x1200')

store = Storage()

store.office_tech(printer_1)
store.office_tech(printer_1)
store.office_tech(printer_2)
store.office_tech(printer_2)
store.office_tech(scanner_1)
store.office_tech(scanner_1)
store.office_tech(scanner_1)
store.office_tech(scanner_2)
store.office_tech(scanner_2)

store.res_dict()
