"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rcj0pB1aB5M

Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:

pt_1 = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа).
При этом в объектах класса Point должны формироваться следующие локальные свойства:

__x, __y - координаты точки на плоскости.

и один геттер:

get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:

r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или

r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний.
При этом, в объектах класса Rectangle (вне зависимости от способа их создания)
должны формироваться следующие локальные свойства:

__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).

Также к классе Rectangle должны быть реализованы следующие методы:

set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника
(ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами:
(x1, y1) (x2, y2)". Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).

P.S. На экран ничего выводить не нужно.
"""


class Point:
    def __init__(self, x, y):
        self.set_coords(x, y)

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float)

    def set_coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            warn_str = f"Координаты должны быть числами!"
            raise ValueError(warn_str)

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if isinstance(args[0], Point) and isinstance(args[1], Point):
            self.x1, self.y1 = args[0].get_coords()
            self.x2, self.y2 = args[1].get_coords()
        else:  # передаются координаты верхн левого и нижнего правого углов прям-ка в явном виде
            pass


if __name__ == '__main__':
    pt_1 = Point(2342, 0.123123)
    pt_2 = Point(234, -0.23243)
    print(pt_1.__dict__)
    print(pt_1.get_coords())
    r1 = Rectangle(pt_1, pt_2)
    print(r1.__dict__)
