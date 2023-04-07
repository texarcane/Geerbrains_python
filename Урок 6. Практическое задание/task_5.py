"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title: str
    _message = 'Start drawing'

    def draw(self):
        print(self._message)


class Pen(Stationery):
    title = 'Pen'
    _message = f'The {title} is writing in the workbook'


class Pencil(Stationery):
    title = 'Pencil'
    _message = f'The {title} is drawing sketch'


class Handle(Stationery):
    title = 'Handle'
    _message = f'The {title} is drawing thick lines on the whiteboard'


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()
