"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/uE1uf7Qtbh4

Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)

Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.)
должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]

P.S. В программе на экран ничего выводить не нужно.
"""


class SingletonFive:
    """
    Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
    Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.)
    должны быть ссылкой на последний (пятый) созданный объект.
    """
    __instance = None
    __instance_counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__instance_counter += 1
        if cls.__instance_counter < 6:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    objs = [SingletonFive(str(n)) for n in range(10)]
    # далее - для само-проверки!
    print(*[(obj_ind + 1, objs[obj_ind], f'obj name is <{objs[obj_ind].name}>')
            for obj_ind in range(len(objs))], sep='\n')
