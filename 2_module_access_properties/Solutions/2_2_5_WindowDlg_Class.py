"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/P0sI_Eb_i0c

Подвиг 5. Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:

wnd = WindowDlg(заголовок окна, ширина, высота)
В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:

__title - заголовок окна (строка);
__width, __height - ширина и высота окна (числа).

В классе WindowDlg необходимо реализовать метод:

show() - для отображения окна на экране (выводит в консоль строку в формате:
"<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").

Также в классе WindowDlg необходимо реализовать два объекта-свойства:

width - для изменения и считывания ширины окна;
height - для изменения и считывания высоты окна.

При изменении размеров окна необходимо выполнять проверку:

- переданное значение является целым числом в диапазоне [0; 10000].

Если хотя бы один размер изменился (высота или ширина),
то следует выполнить автоматическую перерисовку окна (вызвать метод show()).
При начальной инициализации размеров width, height вызывать метод show() не нужно.

P.S. В программе нужно объявить только класс с требуемой функциональностью.
"""


class WindowDlg:
    MIN_VAL = 0
    MAX_VAL = 10000

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @classmethod
    def control_size_value(cls, x):
        return type(x) is int and cls.MIN_VAL <= x <= cls.MAX_VAL

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if self.control_size_value(x=width):
            self.__width = width
            self.show()

    width = property(get_width, set_width)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.control_size_value(x=height):
            self.__height = height
            self.show()

    def show(self):
        print(f"{self.__title}: {self.width}, {self.height}")


# Далее - для проверки!
if __name__ == '__main__':
    wd = WindowDlg('А кто, кто , кто?', 20, 100)
    wd.width = 55
