"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PN3SjHz2ZG4

Подвиг 4. Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model 
для записи и считывания информации о модели автомобиля из локальной приватной переменной __model.

Объект-свойство объявите с помощью декоратора @property. 
Также в объекте-свойстве model должны быть реализованы проверки:

- модель автомобиля - это строка;
- длина строки модели должна быть в диапазоне [2; 100].

Если проверка не проходит, то локальное свойство __model остается без изменений.

Объекты класса Car предполагается создавать командой:

car = Car()
и далее работа с объектом-свойством, например:

car.model = "Toyota"
P.S. В программе объявить только класс. На экран ничего выводить не нужно. 
"""


class Car:

    def __init__(self):
        self.__model = ''

    @classmethod
    def check_model(cls, model):
        return type(model) is str and 2 <= len(model) <= 100

    # @property
    def get_model(self):
        return self.__model

    # @get_model.setter
    def set_model(self, model):
        if self.check_model(model):
            self.__model = model

    model = property(get_model, set_model)


# Далее - для проверки!
if __name__ == '__main__':
    car = Car()
    car.model = 2
    print(car.__dict__)
    car.model = 'BMW'
    print(car.__dict__)
