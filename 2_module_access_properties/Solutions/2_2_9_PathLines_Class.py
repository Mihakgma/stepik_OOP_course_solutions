"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/EAt0fgLNYGg

Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов,
состоящих из линейных сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo.
Объекты этого класса будут формироваться командой:

line = LineTo(x, y)
где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:

x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:

p_1 = PathLines()                   # начало маршрута из точки 0, 0
p_1 = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:

get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов,
а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:

L = sqrt((x1-x0)^2 + (y1-y0)^2)

где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

p_1 = PathLines(LineTo(10, 20), LineTo(10, 30))
p_1.add_line(LineTo(20, -10))
dist = p_1.get_length()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""
from math import sqrt as math_sqrt


class LineTo:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    x = property(get_x, set_x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


class PathLines:
    # начальный объект LineTo
    # FROM = ''
    # суммарная длина всех линий
    LENGTH = 0

    def __init__(self, *args):
        # лист всех объектов
        self.lines = []
        # print(args)
        # self.FROM = args[0]
        [self.add_line(obj) for obj in args]
        self.count_lines_length()

    def add_line(self, line: LineTo):
        self.lines.append(line)
        self.count_lines_length()

    def get_path(self):
        return self.lines

    def get_length(self):
        return self.LENGTH

    @staticmethod
    def count_length(x0, y0, x1, y1):
        """
        длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:
        L = sqrt((x1-x0)^2 + (y1-y0)^2)
        :param x0: x предыдущей точки маршрута
        :param y0: y предыдущей точки маршрута
        :param x1: x текущей точки маршрута
        :param y1: y текущей точки маршрута
        :return:
        """
        return math_sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    def count_lines_length(self):
        tmp_line = LineTo()
        lines_start = list()
        lines_start.append(tmp_line)
        lines = lines_start + self.lines
        lengths = [self.count_length(x0=lines[i].x,
                                     y0=lines[i].y,
                                     x1=lines[i+1].x,
                                     y1=lines[i+1].y)
                   for i in range(len(lines[:-1]))]
        self.LENGTH = sum(lengths)


# Далее - для проверки!
if __name__ == '__main__':
    p_1 = PathLines(LineTo(10, 20), LineTo(10, 30))
    p_1.add_line(LineTo(20, -10))
    dist = p_1.get_length()
    print(dist)
    print(*[(k,v) for (k,v) in p_1.__dict__.items()], sep='\n')

    p_2 = PathLines(LineTo(10, 20))
    dist = p_2.get_length()
    print(dist)
    p_2.add_line(LineTo(20, -10))
    dist = p_2.get_length()
    print(dist)
    print(*[(k, v) for (k, v) in p_2.__dict__.items()], sep='\n')

    p_3 = PathLines(LineTo())
    dist = p_3.get_length()
    print(dist)
