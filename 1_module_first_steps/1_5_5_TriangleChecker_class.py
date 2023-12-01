"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Vr4c1LgE91o

Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:

1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c.
Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).

Sample Input:

3 4 5
Sample Output:

3
"""

from random import randint as random_randint
from pandas import Series as pd_Series


def is_not_number(x):
    out = [True, False][type(x) == int or type(x) == float]
    return(out)


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self, tries_num=100):
        """
        Осуществляет проверку параметров (a, b, c) экземпляра класса TriangleChecker
        :return:
        1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
        2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
        3 - стороны a, b, c образуют треугольник.
        """
        a = self.a
        b = self.b
        c = self.c

        abc = (a, b, c)
        abc_set = set(abc)
        # case 1
        if any([is_not_number(i) for i in abc]):
            return 1
        if any([i <= 0 for i in abc]):
            return 1
        if a + b <= c or b + c <= a or a + c <= b:
            return 2
        return 3


def rnd_int(x_min=-100, x_max=1000):
    return(random_randint(x_min, x_max))


if __name__ == '__main__':
    # далее - для проверки
    check_result = []
    iteration_number = 1000
    for i in range(iteration_number):
        values_lst = [rnd_int(), rnd_int(), rnd_int()]
        # print(f'For <{values_lst}>')
        result = TriangleChecker(*values_lst).is_triangle()
        # print(f'Result is: <{result}>')
        check_result.append(result)
    pd_check_result = pd_Series(check_result)
    print(f'After <{iteration_number}> iterations describe statistics of triangle checking results are:')
    print(pd_check_result.describe())
