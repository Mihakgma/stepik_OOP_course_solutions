"""
1.5 Инициализатор __init__ и финализатор __del__
8 из 11 шагов пройдено
17 из 29 баллов  получено
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI

Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки
(объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table),
два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
"""


class Goods:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Table(Goods):
    pass


class TV(Goods):
    pass


class Notebook(Goods):
    pass


class Cup(Goods):
    pass


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx: int):
        try:
            del self.goods[indx]
        except IndexError:
            print(f'Index must be in <0-{len(self.goods) - 1}> diapason!')

    def get_list(self):
        goods = self.goods
        # return goods
        cart_lst = [f'{gd.name}: {gd.price}' for gd in goods]
        print(cart_lst)


if __name__ == '__main__':
    tb_1 = Table(name='Тогучин', price=9999)
    print(tb_1.__dict__)
    ntb_1 = Notebook(name='пЕтыч', price=29999)
    tv_1 = TV(name='Гном', price=11999)
    cup_1 = Cup(name='Шишига', price=399)
    cart_1 = Cart()
    [cart_1.add(gd=x) for x in [tb_1, ntb_1, tv_1]]
    print(cart_1.__dict__)
    print(cart_1.remove(indx=3))
    print(cart_1.__dict__)
    cart_1.add(gd=cup_1)
    print(cart_1.remove(indx=2))
    print(cart_1.__dict__)
    print(cart_1.get_list())

    cart = Cart()
    [cart.add(x) for x in
     [TV('Samsung', 12990),
      TV('LG', 250),
      Table('Ikea', 10),
      Notebook('Sony', 500),
      Notebook('Apple', 850)]]
    print(cart.__dict__)
