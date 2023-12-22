"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/q_8BdpVWbyE

Подвиг 7. Объявите класс RadiusVector2D, объекты которого должны создаваться командами:

v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)

В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:

__x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).

В классе RadiusVector2D необходимо объявить два объекта-свойства:

x - для изменения и считывания локального атрибута __x;
y - для изменения и считывания локального атрибута __y.

При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:

- значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].

Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0).
Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.

Также в классе RadiusVector2D необходимо объявить статический метод:

norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D
(квадратическая норма вектора: x*x + y*y).

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    COORD_DEFAULT_VALUE = 0

    def __init__(self, x=COORD_DEFAULT_VALUE, y=COORD_DEFAULT_VALUE):
        self.__x = x if self.is_coord_ok(x) else self.COORD_DEFAULT_VALUE
        self.__y = y if self.is_coord_ok(y) else self.COORD_DEFAULT_VALUE

    @classmethod
    def is_coord_ok(cls, coord):
        return type(coord) in (int, float) and cls.MIN_COORD <= coord <= cls.MAX_COORD

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = [self.__x, x][self.is_coord_ok(x)]

    x = property(get_x, set_x)

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = [self.__y, y][self.is_coord_ok(y)]

    y = property(get_y, set_y)

    @staticmethod
    def norm2(vector):
        x, y = vector.x, vector.y
        return x*x + y*y


# Далее - для проверки!
if __name__ == '__main__':
    v1 = RadiusVector2D('fgdfgd')  # радиус-вектор с координатами (0; 0)
    v2 = RadiusVector2D(1)  # радиус-вектор с координатами (1; 0)
    v3 = RadiusVector2D(1, 2)
    v3.x = -10000
    v2.x = ''
    v2.y = 555
    for vec in [v1, v2, v3]:
        print(*[(k, v) for (k, v) in vec.__dict__.items()], sep='\n')
        print()
        # print(*[(k, f'x = {v.x}, y = {v.y}') for (k,v) in vec.__dict__.items()], sep='\n')
