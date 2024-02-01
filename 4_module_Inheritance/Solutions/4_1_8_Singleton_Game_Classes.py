"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PxOfMkw962E

Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными качествами (свойствами).
Как пример, объявите в программе класс с именем:

Singleton

который бы позволял создавать только один экземпляр (все последующие экземпляры должны ссылаться на первый).
Как это делать, вы должны уже знать из этого курса.

Затем, объявите еще один класс с именем:

Game

который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:

game = Game(name)
где name - название игры (строка). В каждом объекте класса Game должен
создаваться атрибут name с соответствующим содержимым.

Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так,
то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

https://stepik.org/lesson/701995/step/8?unit=702096
"""


class Singleton:
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls.__INSTANCE:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE


class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name


if __name__ == '__main__':
    game_1 = Game("Gothic 2: Die Nacht Des Raben")
    game_2 = Game("Divinity: Original Sin 2")
    game_3 = Game("Fable")
    print(game_1, game_1.name)
    print(game_2, game_2.name)
    print(game_3, game_3.name)
