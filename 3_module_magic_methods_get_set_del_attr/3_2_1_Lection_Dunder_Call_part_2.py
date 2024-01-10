import math


class StripChars:
    """
    вызов магического метода __call__ может по сути
    послужить заменой замыкания функции (ий).
    убедиться в истинности этого предположения можно,
    создав класс StripChars,
    который удаляет заданный набор символов в начале и конце строки,
    поданной на вход в качестве агрумента объекту класса-функтора.
    """
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой!!!")
        return args[0].strip(self.__chars)


class Derivate:
    """
    класс-декортатор.
    класс для расчета производной для переданной функции.
    работает по аналогии с декораторами в дополнительном материале к уроку!!!
    """
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


if __name__ == '__main__':
    print("Реализация замыкания с помощью ООП!!!")
    s1 = StripChars(";:<>{}\|/?,.! []")
    print(s1("{}[Hello, World]<> !!"))
    print("Класс-декортатор!!!")
    print(df_sin(math.pi/3))
