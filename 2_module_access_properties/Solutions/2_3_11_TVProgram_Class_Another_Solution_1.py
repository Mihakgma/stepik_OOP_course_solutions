"""
Делаем как нас учили через дескриптор, но если обращение идет через класс, то говорим - это свойство.
Храним программы в dict, так быстрее удалять, а при получении программ отдаем только значения.
"""


class Value:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)


class Telecast:
    uid = Value()
    name = Value()
    duration = Value()

    def __init__(self, uid: int, name: str, duration: int):
        self.uid, self.name, self.duration = uid, name, duration


class TVProgram:
    def __init__(self, name):
        self.name = name
        self.__items = {}

    @property
    def items(self):
        return [val for _, val in sorted(self.__items.items())]

    def add_telecast(self, tl: Telecast):
        self.__items[tl.uid] = tl

    def remove_telecast(self, ind):
        del self.__items[ind]