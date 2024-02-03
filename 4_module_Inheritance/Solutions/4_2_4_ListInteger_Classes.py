"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/pohpzoAbkrQ

Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел.
Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа.
При попытке присвоить любой другой тип данных, генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')
Пример использования класса ListInteger (эти строчки в программе не писать):

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.

https://stepik.org/lesson/701996/step/4?unit=702097
"""


class ListInteger(list):
    def __init__(self, digits: tuple = ()):
        super().__init__()
        [self.append(i) for i in digits]

    def __setitem__(self, key, value):
        self.is_integer(value)
        super().__setitem__(key, value)

    def __str__(self):
        return super().__str__()

    def append(self, x):
        self.is_integer(x)
        super().append(x)

    def is_integer(self, x):
        if type(x) != int:
            raise TypeError('можно передавать только целочисленные значения')


if __name__ == '__main__':
    s = ListInteger((1, 2, 3))
    print(s)
    s[0] = -10
    s.append(11)
    print(s)
    # s[0] = 10.5 # TypeError
