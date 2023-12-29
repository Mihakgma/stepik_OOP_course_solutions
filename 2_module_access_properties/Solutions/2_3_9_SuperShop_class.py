"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/l0U_3dTJZyc

Подвиг 8. Вы начинаете создавать интернет-магазин. Для этого в программе объявляется класс SuperShop,
объекты которого создаются командой:

myshop = SuperShop(название магазина)
В каждом объекте класса SuperShop должны формироваться следующие локальные атрибуты:

name - название магазина (строка);
goods - список из товаров.

Также в классе SuperShop должны быть методы:

add_product(product) - добавление товара в магазин (в конец списка goods);
remove_product(product) - удаление товара из магазина (из списка goods).

Здесь product - это объект класса Product, описывающий конкретный товар.
В этом классе следует объявить следующие дескрипторы:

name = StringValue(min_length, max_length)    # min_length - минимально допустимая длина строки;
max_length - максимально допустимая длина строки
price = PriceValue(max_value)    # max_value - максимально допустимое значение

Объекты класса Product будут создаваться командой:

pr = Product(наименование, цена)
Классы StringValue и PriceValue - это дескрипторы данных. Класс StringValue должен проверять,
что присваивается строковый тип с длиной строки в диапазоне [2; 50], т.е. min_length = 2,
max_length = 50. Класс PriceValue должен проверять,
что присваивается вещественное или целочисленное значение в диапазоне [0; 10000], т.е. max_value = 10000.
Если проверки не проходят, то соответствующие (прежние) значения меняться не должны.

Пример использования класса SuperShop (эти строчки в программе писать не нужно):

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""


class PriceValue:
    min_value = 0
    max_value = 10000

    @classmethod
    def is_correct_price(cls, price):
        return type(price) in (float, int) and cls.min_value <= price <= cls.max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, price):
        if self.is_correct_price(price):
            instance.__dict__[self.name] = price


class StringValue:
    min_length = 2
    max_length = 50

    @classmethod
    def validate(cls, string):
        return type(string) is str and cls.min_length <= len(string) <= cls.max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value


class Product:
    name = StringValue()
    price = PriceValue()
    
    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


if __name__ == '__main__':
    shop = SuperShop("У Балакирева")
    shop.add_product(Product("Курс по Python", 0))
    prod_2 = Product("Курс по Python ООП", 2000)
    shop.add_product(prod_2)
    prod_3 = Product("Курс по Картам Таро", 9999)
    shop.add_product(prod_3)
    for p in shop.goods:
        print(f"{p.name}: {p.price}")
    shop.remove_product(prod_2)
    print(f'\nПосле удаления товара <{prod_2.name}>:')
    for p in shop.goods:
        print(f"{p.name}: {p.price}")
