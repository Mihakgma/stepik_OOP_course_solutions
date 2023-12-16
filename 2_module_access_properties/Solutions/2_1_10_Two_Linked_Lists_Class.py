"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YJiPpHVguyE

Теория по двусвязным спискам (при необходимости): https://youtu.be/0sTH9EwXT1I

Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python),
когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:



Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:

add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:

head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:

__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.

Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:

set_next(self, obj) - изменение приватного свойства __next на значение obj;
set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
get_next(self) - получение значения приватного свойства __next;
get_prev(self) - получение значения приватного свойства __prev;
set_data(self, data) - изменение приватного свойства __data на значение data;
get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:

ob = ObjList("данные 1")
А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
Объявите в программе классы LinkedList и ObjList в соответствии с заданием.

P.S. На экран ничего выводить не нужно.
"""


class LinkedList:
    """
    связный список в целом, который имеет набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """
        добавление нового объекта obj класса ObjList в конец связного списка;
        """
        if not self.head and not self.tail:
            self.head, self.tail = obj, obj
        else:  # список уже содержит как минимум 1 объект
            prev_tail = self.tail
            self.tail = obj
            # реализация привязки к предыдущему и последующему (?) объекту двусв-ого списка!
            prev_tail.set_next(obj)
            obj.set_prev(prev_tail)

    def remove_obj(self):
        """
        удаление последнего объекта из связного списка;
        """
        old_tail = self.tail
        new_tail = old_tail.get_prev()
        if new_tail:
            self.tail = new_tail
            new_tail.set_next(None)
        # в связном списке содержится всего лишь один объект класса ObjList
        else:
            self.head = None
            self.tail = None

    def get_data(self):
        """
        получение списка из строк локального свойства __data всех объектов связного списка.
        """
        head = self.head
        tail = self.tail
        data_container = []
        if not head and not tail:
            pass
        else:
            obj = head
            while obj.get_next():
                data_container.append(obj.get_data())
                obj = obj.get_next()
            data_container.append(obj.get_data())  # берем данные из объекта с пометкой tail
        return data_container

    def get_objects_info(self):
        """
        Получение словаря основных свойств объектов связного списка.
        """
        head = self.head
        tail = self.tail
        obj_container = {}
        if not head and not tail:
            pass
        else:
            obj = head
            # ключ словаря - целое число по порядку!
            counter = 0
            while obj.get_next():
                counter += 1
                obj_container[counter] = get_obj_details(obj)
                obj = obj.get_next()
            else:
                # берем данные из объекта с пометкой tail
                obj_container[counter + 1] = get_obj_details(obj)
        return obj_container


class ObjList:
    """
    приватные локальные свойства:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    """

    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj;
        """
        self.__next = obj

    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj;
        """
        self.__prev = obj

    def get_next(self):
        """получение значения приватного свойства __next;
        """
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev;
        """
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data;
        """
        self.__data = data

    def get_data(self):
        """получение значения приватного свойства __data.
        """
        return self.__data


def get_obj_details(obj: ObjList):
    previous_obj = f'Previous: <{obj.get_prev()}>'
    next_obj = f'Next: <{obj.get_next()}>'
    data = f'Data: <{obj.get_data()}>'
    out = ', '.join([previous_obj, next_obj, data])
    return out


# Далее - проверка правильности работы программы
if __name__ == '__main__':
    lst = LinkedList()
    # возвращает пустой список после инициализации объекта класса LinkedList
    print(LinkedList().get_data())
    # head=tail=None
    print(lst.head == lst.tail, type(lst.head))
    obj_lst_1 = ObjList("данные 1")
    lst.add_obj(obj_lst_1)
    # head=tail=obj
    print(lst.head == lst.tail == obj_lst_1)
    lst.add_obj(ObjList("данные 2"))
    obj_lst_3 = ObjList("данные 3")
    lst.add_obj(obj_lst_3)
    print(*[(f'№{key}', val) for (key, val) in lst.get_objects_info().items()], sep='\n')
    res = lst.get_data()
    print(res)
    lst.remove_obj()
    res = lst.get_data()
    print(res)
    print(*[(f'№{key}', val) for (key, val) in lst.get_objects_info().items()], sep='\n')
    lst_2 = LinkedList()
    obj_lst_5 = ObjList("данные 5")
    lst_2.add_obj(obj=obj_lst_5)
    lst_2.remove_obj()
    print(lst_2.get_data())
