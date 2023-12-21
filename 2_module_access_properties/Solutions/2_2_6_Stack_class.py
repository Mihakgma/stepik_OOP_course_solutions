"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/mg4b8nhVDKY

Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ

Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов),
когда один объект ссылается на следующий и так по цепочке до последнего:



Для этого объявите в программе два класса:

StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:

obj = StackObj(данные)
Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj
должен иметь следующие локальные приватные атрибуты:

__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:

nxt - для записи и считывания информации из локального приватного свойства __next;
data - для записи и считывания информации из локального приватного свойства __data.

При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или значение None.
Если проверка не проходит, то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта односвязного списка
В объектах класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута
__data каждого объекта в порядке их добавления, или пустой список, если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @classmethod
    def check_next(cls, nxt):
        return isinstance(nxt, StackObj) or nxt is None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    data = property(get_data, set_data)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, nxt):
        if self.check_next(nxt):
            self.__next = nxt


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        """
        добавление объекта класса StackObj в конец односвязного списка
        :param obj: StackObj
        :return: None
        """
        if self.top is None:
            self.top = obj
            self.last = obj
        else:
            self.last.next = obj
            self.last = obj

    def pop(self):
        """
        извлечение последнего объекта с его удалением из односвязного списка
        :return: None
        """
        top = self.top
        if top is None:
            return
        last = self.last
        next_obj = top.next
        pre_last = top
        if not next_obj:
            self.top = None
            self.last = None
            return last
        while next_obj != last:
            pre_last = next_obj
            next_obj = next_obj.next
        pre_last.next = None
        self.last = pre_last
        return last

    def get_data(self):
        """
        :return: lst(obj: StackObj) список из объектов односвязного списка
        (список из строк локального атрибута __data каждого объекта в порядке их добавления
        или пустой список, если объектов нет)
        """
        out_data = []
        top = self.top
        if not top:
            return out_data
        if not top.next:
            out_data.append(top.data)
            return out_data
        obj = top
        while obj:
            out_data.append(obj.data)
            obj = obj.next
        return out_data


# Далее - для проверки!
if __name__ == '__main__':
    st = Stack()
    st.push(StackObj("obj1"))
    st.push(StackObj("obj2"))
    st.push(StackObj("obj3"))
    st.pop()
    res = st.get_data()
    print(res)
    print(*[(k,v.next) for (k,v) in st.__dict__.items()], sep='\n')
