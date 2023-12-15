class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.set_coords(*args)
        elif len(args) == 4:
            x1, y1, x2, y2 = args
            self.set_coords(Point(x1, y1), Point(x2, y2))

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        x1, y1, x2, y2 = self.__sp, self.__ep
        print(f'Прямоугольник с координатами: ({x1}, {y1}) ({x2}, {y2})')


if __name__ == '__main__':
    rect = Rectangle(0, 0, 20, 34)
