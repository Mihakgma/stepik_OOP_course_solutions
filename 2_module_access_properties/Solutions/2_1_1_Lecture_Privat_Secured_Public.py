"""
https://www.youtube.com/watch?v=RipfqbH0eqY
"""


class Point:
    COORDS_RANGE = [i for i in range(-100, 101)]

    def __init__(self, x=0, y=0):
        self.set_coords(x, y)

    @classmethod
    def __check_value(cls, value):
        min_val = min(cls.COORDS_RANGE)
        max_val = max(cls.COORDS_RANGE)
        return ((type(value) in (int, float)) and
                min_val <= value <= max_val)

    def set_coords(self, x, y):
        digits_range = self.COORDS_RANGE
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            warn_str = f"Координаты должны быть числами в диапазоне от {min(digits_range)} до {max(digits_range)}!"
            raise ValueError(warn_str)


coords = {
    1: [(-1000, 'y_val')],
    2: [(100, -301)],
    3: [(-0.99, 55)],
    4: [('three', True)],
    5: [(True, False)],
    6: [(3, -0.5)],
    7: [(99, '-35')]
}


def create_point(key: int, coords: tuple):
    try:
        pt = Point(*coords)
        return (key, pt)
    except ValueError as e:
        print(f'For <{key}> ValueError has been occured: <{e}>')
        return (key, None)


if __name__ == '__main__':
    [val.append(create_point(key, val[0])[1]) for key, val in coords.items()]
    print()
    print(*[(key, val) for (key, val) in coords.items()], sep='\n')
