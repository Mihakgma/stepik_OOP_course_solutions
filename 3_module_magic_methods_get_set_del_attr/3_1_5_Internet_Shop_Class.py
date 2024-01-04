"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DVydksYIejk

Подвиг 4. Вы создаете интернет-магазин. Для этого нужно объявить два класса:

Shop - класс для управления магазином в целом;
Product - класс для представления отдельного товара.

Объекты класса Shop следует создавать командой:

shop = Shop(название магазина)
В каждом объекте класса Shop должно создаваться локальное свойство:

goods - список товаров (изначально список пустой).

А также в классе объявить методы:

add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
remove_product(self, product) - удаление товара product из магазина (из списка goods);

Объекты класса Product следует создавать командой:

p = Product(название, вес, цена)
В них автоматически должны формироваться локальные атрибуты:

id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
name - название товара (строка);
weight - вес товара (целое или вещественное положительное число);
price - цена (целое или вещественное положительное число).

В классе Product через магические методы (подумайте какие) осуществить проверку
на тип присваиваемых данных локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.).
Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id.
При попытке это сделать генерировать исключение:

raise AttributeError("Атрибут id удалять запрещено.")
Пример использования классов (в программе эти строчки не писать):

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
P.S. На экран ничего выводить не нужно.
"""


class Product:
    """
    check_attrs_info, где:
    ключ - наименование атрибута
    значение список из:
        а) лист допустимых типов данных для атрибута
        б) минимальное значение
        в) метка (bool) возможности удаления атрибута
    """
    MAX_ID = 0
    check_attrs_info = {
        "id": [[int], 1, False],
        "name": [[str], "", True],
        "weight": [[int, float], 0, True],
        "price": [[int, float], 0, True]
    }

    def __new__(cls, *args, **kwargs):
        cls.MAX_ID += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self.MAX_ID

    def __setattr__(self, key, value):
        check_ok = [True for (k, v) in self.check_attrs_info.items()
                    if key == k and type(value) in v[0] and value >= v[1]]
        if check_ok:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        attrs_couldntbe_deleted = [k for (k, v) in self.check_attrs_info.items()
                                   if not v[2]]
        # print(attrs_couldntbe_deleted)
        if item in attrs_couldntbe_deleted:
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
        else:
            object.__delattr__(self, item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


# Далее - для проверки!
if __name__ == '__main__':
    shop = Shop("Балакирев и К")
    book = Product("Python ООП", 100, 1024)
    shop.add_product(book)
    shop.add_product(Product("Python", 150, 512))
    shop.add_product(Product("C++ для чайников", 350, 1512))
    shop.remove_product(product=book)
    for p in shop.goods:
        print(f"{p.id} {p.name}, {p.weight}, {p.price}")
    # print(Product.__dict__)
    print(*[(k, v) for (k, v) in Product.__dict__.items()], sep='\n')
    book.id = 100
    print()
    print(*[(k, v) for (k, v) in book.__dict__.items()], sep='\n')
    print("Пробуем удалять атрибут объекта")
    # del book.id
    del book.name
    print(*[(k, v) for (k, v) in book.__dict__.items()], sep='\n')
