"""
dunder-методы методы с двойным подчеркиванием с обеих сторон:

__str__() - для отображения информации об объекте класса для
пользователей (напр. для функции print, str)

__repr__() - для отображения информации об объекте класса в режиме отладки (для разработчиков)

__len__() - позволяет применять функцию len() к экземплярам класса

__abs__() - то же самое, только для ф-ции abs()
"""


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


class Point:
    def __init__(self, *args):
        """
        Точка в n-мерном пространстве.
        Количество размерностей определяется количеством поданнымх координат
        :param args: переданные координаты
        """
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


if __name__ == '__main__':
    red_cat = Cat(name="Кузя")
    print(red_cat.__repr__())
    print(red_cat)
    print(str(red_cat))

    p = Point(-1, 2, -5.903423)
    print(len(p))
    print(abs(p))
