"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/bPH4It1_d0c

Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse.
Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов
(произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол)
и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно
(или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения).
Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
"""
from random import choice as random_choice
from random import randint as random_randint


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


def rnd_int(x_min=-1000, x_max=1000):
    return(random_randint(x_min, x_max))


if __name__ == '__main__':
    figures_classes = [Line(*[0]*4), Rect(*[rnd_int()]*4), Ellipse(*[rnd_int()]*4)]
    elements = [random_choice(figures_classes) for i in range(217)]
    # далее - для проверки
    print(random_choice(figures_classes).__dict__)
    print(f'Длина списка случайных фигур составила: <{len(elements)}>')
    print(*[i.__dict__ for i in elements], sep='\n')
