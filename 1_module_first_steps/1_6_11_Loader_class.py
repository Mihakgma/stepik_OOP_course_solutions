"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/5aJVuJ5jGqk

Подвиг 10 (на повторение материала). В программе предполагается реализовать парсер (обработчик)
строки (string) в определенный выходной формат. Для этого объявлен следующий класс:

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

И предполагается его использовать следующим образом:

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())

На выходе (в переменной res) ожидается получить список из набора вещественных чисел.
Например, для заданной строки, должно получиться:

[4.0, 5.0, -6.5]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя методами:

build_sequence(self) - для создания начального пустого списка (метод должен возвращать пустой список);
build_number(self, string) - для преобразования переданной в метод строки (string) в
вещественное значение (метод должен возвращать полученное вещественное число).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно.
"""
from random import random as rnd_random
from random import randint as rnd_randint


# Здесь объявляется класс Factory
class Factory:
    def __init__(self):
        pass

    def build_sequence(self):
        return list()

    def build_number(self, string):
        return float(string.strip())


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


def gener_rand_floats(n: int,
                      separator: str=', ',
                      decimal_number: str=2):
    """
    :param n: количество дробными чисел в строке
    :return: строка с дробными числами с заданным разделителем
    """
    out_str = separator.join([str(round(rnd_random()*rnd_randint(-100, 100), decimal_number))
                              for i in range(n)])
    return out_str



if __name__ == '__main__':
    # эти строчки не менять!
    ld = Loader()
    # s = input()
    # res = ld.parse_format(s, Factory())
    # Далее - код для проверки!
    s = gener_rand_floats(n=115)
    res = ld.parse_format(s, Factory())
    print(*res, sep='\n')
