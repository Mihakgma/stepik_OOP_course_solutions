"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/sX_uP7GVqkc

Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:

dlg = Dialog(<название>)

Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.

Класс Dialog должен создавать объекты класса DialogWindows, если переменная
TYPE_OS = 1 и объекты класса DialogLinux, если переменная TYPE_OS не равна 1.
При этом, переменная TYPE_OS может меняться в последующих строчках программы.
Имейте это в виду, при объявлении класса Dialog.

P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.
"""


TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    __os_dialog = None

    def __new__(cls, *args, **kwargs):
        # global TYPE_OS
        cls.__os_dialog = [super().__new__(DialogWindows),
                           super().__new__(DialogLinux)][TYPE_OS != 1]
        setattr(cls.__os_dialog, 'name', args[0])
        return cls.__os_dialog


if __name__ == '__main__':
    name = 'хэзэшечка'
    dlg = Dialog(name)
    # Далее - для самопроверки!!!
    name = 'хэзэшечка'
    dlg_1 = Dialog(name)
    print(dlg_1.__dict__, dlg_1)

    TYPE_OS = 2

    name_2 = 'нямочка'
    dlg_2 = Dialog(name_2)
    print(dlg_2.__dict__, dlg_2)
