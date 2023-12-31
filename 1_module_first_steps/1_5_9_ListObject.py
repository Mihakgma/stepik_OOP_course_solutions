"""
import hashlib


if __name__ == '__main__':
    match "hello world":
        case "hello world" as f:
            print(hashlib.sha256(f.encode()).hexdigest())



Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/3WfWCBKRKIM

Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ

Подвиг 9. Вам необходимо реализовать односвязный список (не список языка Python,
объекты в списке не хранить, а формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:



Для этого объявите в программе класс ListObject, объекты которого создаются командой:

obj = ListObject(buffer)
Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
buffer - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self
(то есть, атрибут next_obj объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Затем сформируйте односвязный список, в объектах которых (в атрибуте buffer) хранятся строки из списка lst_in
(первая строка в первом объекте, вторая - во втором и  т.д.).
На первый добавленный объект класса ListObject должна ссылаться переменная head_obj.

P.S. В программе что-либо выводить на экран не нужно.

Sample Input:

1. Первые шаги в ООП
1.1 Как правильно проходить этот курс
1.2 Концепция ООП простыми словами
1.3 Классы и объекты. Атрибуты классов и объектов
1.4 Методы классов. Параметр self
1.5 Инициализатор init и финализатор del
1.6 Магический метод new. Пример паттерна Singleton
1.7 Методы класса (classmethod) и статические методы (staticmethod)
Sample Output:
"""


class ListObject:
    def __init__(self, next_obj=None, data: str = ''):
        self.next_obj = next_obj
        self.data = data

    def link(self, obj):
        self.next_obj = obj


def create_list_obj(obj_data_lst):
    objects_lst = [ListObject(data=i) for i in obj_data_lst]
    head = objects_lst[0]
    for obj_index in range(len(objects_lst)):
        obj = objects_lst[obj_index]
        try:
            obj_nxt = objects_lst[obj_index + 1]
            obj.link(obj=obj_nxt)
        except IndexError:
            print('End of a list!')
    return objects_lst, head


if __name__ == '__main__':
    lst_in = ['1. Первые шаги в ООП',
              '1.1 Как правильно проходить этот курс',
              '1.2 Концепция ООП простыми словами',
              '1.3 Классы и объекты. Атрибуты классов и объектов',
              '1.4 Методы классов. Параметр self',
              '1.5 Инициализатор init и финализатор del',
              '1.6 Магический метод new. Пример паттерна Singleton',
              '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
    obj_lst, head_obj = create_list_obj(obj_data_lst=lst_in)
    # print([i.__dict__ for i in obj_lst_3], sep='\n')
    print('\n'.join([str(i.__dict__) for i in obj_lst]))
