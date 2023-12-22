class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2

    def __init__(self, x=0, y=0):
        self.__x = x if self.validate(x) else 0
        self.__y = y if self.validate(y) else 0

    def validate(self, n):
        return isinstance(n, (int, float)) and self.MIN_COORD <= n <= self.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, n):
        self.__x = [self.__x, n][self.validate(n)]

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, n):
        self.__y = [self.__y, n][self.validate(n)]


# Далее - для проверки!
if __name__ == '__main__':
    v1 = RadiusVector2D('fgdfgd')  # радиус-вектор с координатами (0; 0)
    v2 = RadiusVector2D(1)  # радиус-вектор с координатами (1; 0)
    v3 = RadiusVector2D(1, 2)
    v3.x = -10000
    v2.x = ''
    v2.y = 555
    for vec in [v1, v2, v3]:
        print(*[(k, v) for (k, v) in vec.__dict__.items()], sep='\n')
        print()
