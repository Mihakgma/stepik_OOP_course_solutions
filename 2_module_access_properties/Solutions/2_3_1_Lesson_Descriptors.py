"""
Песнь 9. Дескрипторы (data descriptor и non-data descriptor)
https://stepik.org/lesson/701985/step/1?unit=702086
"""


class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть числом!")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value


class Point3D:
    x, y, z = (Integer() for i in range(3))

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    p = Point3D(1, 2, 3)
    p.z = 777
    print(p.__dict__)
    p_1 = Point3D(11, 22, '')
    print(p_1.__dict__)
