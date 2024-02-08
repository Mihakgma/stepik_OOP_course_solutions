"""
Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs,
который бы позволял обращаться к локальным атрибутам объектов дочерних классов по индексу.
Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости.
Объекты этого класса должны создаваться командой:

pt = Point(x, y)
где x, y - целые или вещественные числа.

Пример использования классов (эти строчки в программе не писать):

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""


class ItemAttrs(list):
    def __init__(self, *args):
        super().__init__()
        [self.append(i) for i in args]


#         elif len(kwargs):
#             [self.append(v) for (k,v) in kwargs.items()]

#     def __getitem__(self, *args):
#         return self[args[0]]

#     def __setitem__(self, key, value):
#         return super().__setitem__(key, value)


class Point(ItemAttrs):
    pass
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.x = x
#         self.y = y
#         # [self.append(v) for (k,v) in self.__dict__.items()]


if __name__ == '__main__':
    item = Point(1, 2)
    print(item)
    item[1] = 3
    item[1]
    