"""
Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:

air = Aircraft(model, mass, speed, top)
где model - модель самолета (строка); mass - подъемная масса самолета
(любое положительное число); speed - максимальная скорость (любое положительное число);
top - максимальная высота полета (любое положительное число).

В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами:
_model, _mass, _speed, _top и соответствующими значениями.
Если передаваемые аргументы не соответствуют указанным критериям
(строка, любое положительное число), то генерируется исключение командой:

raise TypeError('неверный тип аргумента')
Далее, в программе объявите следующие дочерние классы:

PassengerAircraft - пассажирский самолет;
WarPlane - военный самолет.

Объекты этих классов создаются командами:

pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест (целое положительное число)
wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь); ключи - название оружия,
значение - количество
В каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты с именами
_chairs и _weapons соответственно. Инициализация остальных атрибутов должна выполняться
через инициализатор базового класса.

В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов chairs и weapons.
Если тип данных не совпадает, то генерировать исключение командой:

raise TypeError('неверный тип аргумента')
Создайте в программе четыре объекта самолетов со следующими данными:

PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}

Все эти объекты представить в виде списка planes.

P.S. В программе нужно объявить только классы и сформировать список На экран выводить ничего не нужно.

https://stepik.org/lesson/701998/step/9?unit=702099
"""


class Descriptor:
    _ObjectType = ()
    _MinValue = 0

    def __init__(self):
        self._object_type = self._ObjectType
        self._min_value = self._MinValue

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        # print(self._object_type, self._min_value)
        # print(value)
        if type(value) in self._object_type and value > self._min_value:
            setattr(instance, self.name, value)
        else:
            raise TypeError('неверный тип аргумента')
            # raise TypeError(f'неверный тип аргумента <{value}>')


class String(Descriptor):
    _ObjectType = (str,)
    _MinValue = ""


class PositiveDigit(Descriptor):
    _ObjectType = (int, float)
    _MinValue = 0


class PositiveInteger(Descriptor):
    _ObjectType = (int,)
    _MinValue = 0


class WeaponsDict(Descriptor):
    _ObjectType = (dict,)
    _MinValue = 0

    def __set__(self, instance, value):
        ok = False
        if type(value) in self._object_type and len(value) > self._min_value:
            if all([((type(k) == str) + (type(v) == int and v > self._min_value)) == 2
                    for (k, v) in value.items()]):
                setattr(instance, self.name, value)
                ok = True
        if not ok:
            raise TypeError('неверный тип аргумента')


class Aircraft:
    model, mass, speed, top = String(), *[PositiveDigit() for i in range(3)]

    # print(model, mass, speed, top)
    def __init__(self, model=model, mass=mass, speed=speed, top=top):
        self.model, self.mass, self.speed, self.top = model, mass, speed, top


class PassengerAircraft(Aircraft):
    model, mass, speed, top, chairs = String(), *[PositiveDigit() for i in range(3)], PositiveInteger()

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.chairs = chairs


class WarPlane(Aircraft):
    model, mass, speed, top, weapons = String(), *[PositiveDigit() for i in range(3)], WeaponsDict()

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.weapons = weapons


if __name__ == '__main__':
    # air = Aircraft('model', 1, 2, 3)
    # assert air._model == 'model' and air._mass == 1 and air._speed == 2 and air._top == 3  # , "неверные значения атрибутов объекта класса Aircraft"
    #
    # # air = Aircraft('4', 1, -2, 3)
    # try:
    #     air = Aircraft('4', 1, -2, 3)
    # except TypeError:
    #     assert True
    # else:
    #     assert False  # , "не сгенерировалось исключение TypeError при выполнении команды Aircraft('4', 1, -2, 3)"
    # print(air.__dict__)
    # # PassengerAircraft('model', 1, 2, 3, -7)
    # try:
    #     PassengerAircraft('model', 1, 2, 3, 0.2)
    # except TypeError:
    #     assert True
    # else:
    #     assert False  # , "не сгенерировалось исключение TypeError при выполнении команды PassengerAircraft('model', 1, 2, 3, 0)"

    # wp_1 = WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10.0})
    # wp_2 = WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
    # print(wp_1.__dict__)
    # print(wp_2.__dict__)

    planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
              PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
              WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
              WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
    for plane in planes:
        print()
        print(*[(k,v) for (k,v) in plane.__dict__.items()], sep="\n")
