"""
переписываем атрибуты через одно подчеркивание
и тогда метод get_coords() будет работать даже, если
его определить в дочернем классе!

"""


class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор класса: <{self.__class__}>")
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill="red"):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    def get_coords(self):
        """
        доступ к атрибутам (protected) открыт
        для использования даже из дочерних классов!
        """
        return self._x1, self._y1, self._x2, self._y2


if __name__ == '__main__':
    r = Rect(0, 0, 10, 20)
    print(r.__dict__)
    print(r.get_coords())
    # print(r._x1)  # так обращаться к ним не следует!!!