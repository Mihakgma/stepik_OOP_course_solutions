"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/vOh4gzHnMWg

Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно проверять,
что присваиваемые значения - числа (целые или вещественные). Дополнительно у радиуса проверять,
что число должно быть положительным (строго больше нуля). Сделать все эти проверки нужно через магические методы.
При некорректных переданных числовых значениях, прежние значения меняться не должны
(исключений никаких генерировать при этом не нужно).

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.

Пример использования класса (эти строчки в программе писать не нужно):

circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
P.S. На экран ничего выводить не нужно.
"""
from math import inf as math_inf


class Circle:
    __ATTRIBUTE_DETAILS = {
        "__x": [[int, float], -math_inf],
        "__y": [[int, float], -math_inf],
        "__radius": [[int, float], 0]
    }

    def __init__(self, x, y, radius):
        self.__setattr__(key='__x', value=x)
        # self.x = x
        # self.y = y
        # self.radius = radius

    def __getattr__(self, item):
        print(f"Сработал __getattr__ при попытке обращения к <{item}> - несуществующему атрибуту экз класса!")
        return False

    def __setattr__(self, key, value):
        print(f"Попытка присвоить атрибуту <{key}> значения <{value}>")
        if [True for (k, v) in self.__ATTRIBUTE_DETAILS.items()
        if key == k and type(value) not in v[0]]:
            raise TypeError("Неверный тип присваиваемых данных.")
        check_ok = [True for (k, v) in self.__ATTRIBUTE_DETAILS.items()
                    if key == k and value > v[1]]
        if check_ok:
            object.__setattr__(self, key, value)
        else:
            # игнорируем неверное численное значение - ничего не происходит
            print(f"Игнорим <{value}> для <{key}>")
            # object.__setattr__(self, key, 0)
            pass

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    x = property(get_x, set_x)

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    y = property(get_y, set_y)

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    radius = property(get_radius, set_radius)


# Далее - для проверки!
if __name__ == '__main__':
    circle = Circle(10.5, 7, 22)
    circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    print("\nПроверка по присвоению атрибутам корректных / некорректных значений:")
    # print(*[(k, v) for (k, v) in circle.__dict__.items()], sep='\n')
    x, y, r = circle.x, circle.y, circle.radius
    print(x, y, r)
    res = circle.name  # False, т.к. атрибут name не существует
    print(res)
