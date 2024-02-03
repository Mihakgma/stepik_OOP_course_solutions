"""
Лекция "Песнь 20. Функция issubclass(). Наследование от встроенных типов и от object"

https://stepik.org/lesson/701996/step/1?auth=registration&unit=702097



"""


class Geom:
    pass


class Line(Geom):
    pass


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


class SmartPhone:
    pass


class IPhone(SmartPhone):
    pass


if __name__ == '__main__':
    g = Geom()
    print(g)
    l = Line()
    # свойство (атрибут) класс наслед-ся от обжект
    print(l.__class__)
    # функция issubclass() работает только с ниамиенованиями классов, а не с их экземплярами!
    print(issubclass(Geom, object))
    print(issubclass(Line, Geom))
    print(issubclass(Line, object))
    print(issubclass(int, object))
    v = Vector([1, 2, 3])
    v.append(4)
    print(v)
    v.pop()
    print(v)
    print()

    phone = IPhone()

    print(isinstance(phone, SmartPhone))
    print(issubclass(IPhone, object))
    print(issubclass(SmartPhone, IPhone))
