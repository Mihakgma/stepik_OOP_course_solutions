class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius
        if radius <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, val):
        if val > 0:
            self.__radius = val

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            return object.__setattr__(self, key, value)
        raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False
