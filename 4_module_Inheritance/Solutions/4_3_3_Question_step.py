"""
Выберите все верные утверждения, связанные с этой программой:

в классе IPhone выполняется переопределение метода get_info()

в методе get_info() класса SmartPhone выполняется делегированый вызов метода get_info() класса IPhone

в методе get_info() класса IPhone выполняется делегированый вызов метода get_info() класса SmartPhone

класс IPhone лишь переопределяет класс SmartPhone

класс IPhone расширяет класс SmartPhone
"""


class SmartPhone:
    def call(self):
        pass

    def get_info(self):
        return "SmartPhone"


class IPhone(SmartPhone):
    def __init__(self, model):
        self.model = model

    def get_info(self):
        return super().get_info() + ": IPhone " + self.model
