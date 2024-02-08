"""
https://stepik.org/lesson/701998/step/1?unit=702099

https://www.youtube.com/watch?v=zHgPAm-imvY
"""


# Коммент от Степана
# https://stepik.org/lesson/701998/step/1?discussion=8353356&unit=702099
class First:

    def __init__(self, val1):
        self.first = val1

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        self.__first = value


class Descriptor:

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Second(First):

    second = Descriptor()

    def __init__(self, val1, val2=second):
        super().__init__(val1)
        self.second = val2


class Third(Second):

    def __init__(self, val1, val2, val3):
        super().__init__(val1, val2)
        self.third = val3


class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор класса: <{self.__class__}>")
        self.__x1, self.__y1, self.__x2, self.__y2 = x1, y1, x2, y2

    def get_coords(self):
        """
        Если прописать данный метод в дочернем классе Rect
        и попробовать вызвать его, то возникнет ошибка AttributeError
        т.к. атрибуты с данными именами (private) отсутствуют
        в дочернем классе из-за префикса (перед двойным подчеркиавнием) родительского.
        """
        return self.__x1, self.__y1, self.__x2, self.__y2


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill="red"):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill


if __name__ == '__main__':
    one = First('first')
    two = Second('first', 'second')
    three = Third('first', 'second', 'third')

    print(three.first)  # first
    print(three.second)  # second
    print(three.__dict__)  # {'_First__first': 'first', '__second': 'second', 'third': 'third'}

    print("Выполнение кода из лекции:\n")
    r = Rect(0, 0, 10, 20)
    print(r.__dict__)
    print(r.get_coords())