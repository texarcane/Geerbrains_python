"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumbers:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def __add__(self, other):
        return ComplexNumbers(self.value_1 + other.value_1, self.value_2 + other.value_2)

    def __mul__(self, other):
        return ComplexNumbers((self.value_1 * other.value_1 - self.value_2 * other.value_2),
                              (self.value_1 * other.value_2 + self.value_2 * other.value_1))

    def __str__(self):
        return f'{self.value_1}{"+" if self.value_2 > 0 else ""}{self.value_2}i'


c_num_1 = ComplexNumbers(17, 76)
c_num_2 = ComplexNumbers(18, 12)

print(c_num_1+c_num_2)
print(c_num_1*c_num_2)
