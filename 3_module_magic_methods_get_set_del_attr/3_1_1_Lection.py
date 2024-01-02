"""
https://www.youtube.com/watch?v=CAx-NLFc-Z4
https://proproprogs.ru/python_oop/magicheskie-metody-setattr-getattribute-getattr-i-delattr
"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MAX_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left
    def __getattribute__(self, item):
        """
        Переопределяя данный магический метод мы можем управлять доступом к тому или иному атрибуту объекта класса
        :param item: наименование атрибута / метода (?)
        :return: значение атрибута
        """
        if item == "x":
            raise ValueError("доступ запрещен!")
        # print("__getattribute__")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """
        Переопределяя данный магич. метод мы имеем возможность управлять переприсвоением значений атрибутам
        :param key: наименование атрибута
        :param value: новое значение атрибута
        :return: None
        """
        if key == "z":
            raise AttributeError("Недопустимое имя атрибута!")
        print(f"worked  __setattr__ for <{key}>")
        object.__setattr__(self, key, value)
        # так переприсваивать значение атрибута можно, но - не желательно!
        # self.__dict__[key] = value

    def __getattr__(self, item):
        """
        Вызывается каждый раз, когда происходит обращение к несуществющему отрибуту экземпляра класса!
        :param item: наименование атрибута
        :return: False
        """
        print(f"Попытка обращения к несуществующему атрибуту экземпляра класса: <{item}>")
        return False

    def __delattr__(self, item):
        """
        Вызывается при удалении атрибута. Для управлением процессом удаления атрибута объекта класса
        :param item: наименование атрибута
        :return: None
        """
        print(f"worked __delattr__ for <{item}>")
        object.__delattr__(self, item)


if __name__ == '__main__':
    pt_1 = Point(1, 2)
    pt_2 = Point(10, 20)
    a = pt_1.y
    print(a)
    print(pt_1.yy)
    print(pt_1.MAX_COORD)
    del pt_1.x
    print(pt_1.__dict__)
    # pt_1.z = 5
    # pt_1.set_bound(-100)
    # print(pt_1.__dict__)
    # print(Point.__dict__)
