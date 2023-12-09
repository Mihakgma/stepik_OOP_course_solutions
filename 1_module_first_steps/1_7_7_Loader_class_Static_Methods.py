"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/KV8T8JDtxW4

Подвиг 6. В программе предполагается реализовать парсер (обработчик) строки с данными string в
определенный выходной формат. Для этого объявлен следующий класс:

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq
И предполагается его использовать следующим образом:

res = Loader.parse_format("4, 5, -6", Factory)
На выходе (в переменной res) ожидается получать список из набора целых чисел. Например, для заданной строки,
должно получиться:

[4, 5, -6]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:

build_sequence() - для создания пустого списка (метод возвращает пустой список);
build_number(string) - для преобразования строки (string) в целое число
(метод возвращает полученное целочисленное значение).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно.
"""
from random import random as rnd_random
from random import randint as rnd_randint


# Здесь объявляется класс Factory
class Factory:
    def __init__(self):
        pass

    @staticmethod
    def build_sequence():
        return list()

    @staticmethod
    def build_number(string):
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
