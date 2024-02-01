"""
Подвиг 4. Наследование часто используют, чтобы вынести общий код дочерних классов в базовый класс. Сделаем такой пример.
Объявите в программе базовый класс Animal (животное), объекты которого можно создать командой:

an = Animal(name, old)
где name - название животного (строка); old - возраст животного (целое число).
Такие же локальные атрибуты (name и old) должны создаваться в объектах класса.

Далее, объявите дочерний класс (от базового Animal) с именем Cat (кошки), объекты которого создаются командой:

cat = Cat(name, old, color, weight)
где name, old - те же самые параметры, что и в базовом классе;
color - цвет кошки (строка);
weight - вес кошки (любое положительное число).

В объектах класса Cat должны автоматически формироваться локальные атрибуты: name, old, color, weight.
Формирование атрибутов name, old должен выполнять инициализатор базового класса.

По аналогии объявите еще один дочерний класс Dog (собака), объекты которого создаются командой:

dog = Dog(name, old, breed, size)
здесь name, old - те же самые параметры, что и в базовом классе;
breed - порода собаки (строка);
size - кортеж в формате (height, length) высота и длина - числа.

В объектах класса Dog по аналогии должны формироваться локальные атрибуты: name, old, breed, size.
За формирование атрибутов name, old отвечает инициализатор базового класса.

Наконец, в классах Cat и Dog объявите метод:

get_info() - для получения информации о животном.

Этот метод должен возвращать строку в формате:

"name: old, <остальные параметры через запятую>"

Например, для следующего объекта класса Cat:

cat = Cat('кот', 4, 'black', 2.25)
метод get_info должен вернуть строку:

"кот: 4, black, 2.25"

P.S. В программе достаточно объявить три класса. Выводить на экран ничего не нужно.

https://stepik.org/lesson/701995/step/5?unit=702096

ПроверОчки :-D:
1) name в выводе метода get_info() - всегда на первом месте во всех дочерних классах;
2) низзя вызывать метод get_info() в родительском классе Animal!
"""


class Animal:
    def __init__(self, name, old):
        self.name, self.old = name, old

    def get_info(self):
        if self.__class__.__name__ == "Animal":
            raise NotImplementedError
        attrs_str = ", ".join([str(v) for (k, v) in self.__dict__.items() if k != "name"])
        return self.name + ": " + attrs_str


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size


class Fox(Animal):
    def __init__(self, zoo_id, name, old, breed, size):
        super().__init__(name, old)
        self.zoo_id = zoo_id
        self.breed = breed
        self.size = size


if __name__ == '__main__':
    jack = Dog("Jack", 5, "лайка", (50, 75))
    print(jack.get_info())                                          # Jack: 5, лайка, (50, 75)
    fox = Fox(1, "Reddy", 3, "сибирская пушистохвостая", (20, 55))
    print(fox.get_info())                                           # Reddy: 3, 1, сибирская пушистохвостая, (20, 55)
    level_boss = Animal("соловей-разбойник", 666)
    # print(level_boss.get_info())                                    # NotImplementedError
