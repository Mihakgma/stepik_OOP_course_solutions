"""
Выберите все верные утверждения, связанные с этой программой:

класс Phone расширяет класс SmartPhone

в классе SmartPhone выполняется переопределение метода get_info()

класс SmartPhone лишь переопределяет класс Phone

класс SmartPhone наследуется от класса Phone

дочерний класс SmartPhone расширяет базовый класс Phone
"""


class Phone:
    def get_info(self):
        return "Phone"


class SmartPhone(Phone):
    def call(self):
        pass

    def get_info(self):
        return "SmartPhone"

