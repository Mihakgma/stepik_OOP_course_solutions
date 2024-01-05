"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/FaHqn8Yr45o

Подвиг 10. Объявите класс GeyserClassic - фильтр для очистки воды. В этом классе должно быть три слота для фильтров.
Каждый слот строго для своего класса фильтра:

Mechanical - для очистки от крупных механических частиц;
Aragon - для последующей очистки воды;
Calcium - для обработки воды на третьем этапе.



Объекты классов фильтров должны создаваться командами:

filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)
Во всех объектах этих классов должен формироваться локальный атрибут:

date - дата установки фильтров (для простоты - положительное вещественное число).

Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение).
В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.

Объекты класса GeyserClassic должны создаваться командой:

g = GeyserClassic()
А сам класс иметь атрибут:

MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)

и следующие методы:

add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3),
если он (слот) пустой (без фильтра). Также здесь следует проверять,
что в первый слот можно установить только объекты класса Mechanical,
во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.

remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);

get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);

water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.

Метод water_on() должен возвращать значение True при выполнении следующих условий:

- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть
в пределах [0; MAX_DATE_FILTER])

Пример использования классов  (эти строчки в программе писать не нужно):

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
P.S. На экран ничего выводить не нужно.
"""
import time


class Filter:
    def __init__(self, date):
        self.date = date
        self.filter_installed = True

    def __setattr__(self, key, value):
        if key == "filter_installed":
            object.__setattr__(self, key, value)
        elif "filter_installed" not in self.__dict__:
            if key == "date" and isinstance(value, float) and value >= 0:
                object.__setattr__(self, key, value)
        else:
            pass
            # print(f"Невозможно переприсвоить значение <{value}> для атрибута <{key}>")


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    filters_codes = {
        1: Mechanical,
        2: Aragon,
        3: Calcium
    }

    def __init__(self):
        self.filters_installed = {
            1: None,
            2: None,
            3: None
        }

    @classmethod
    def verify_filter(cls, slot_num, filter=False):
        filters = cls.filters_codes
        if not filter:
            return slot_num in filters
        if slot_num in filters and [True for (k, v) in filters.items()
                                    if k == slot_num and v == type(filter)]:
            return True

    def add_filter(self, slot_num, filter):
        """
        добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3),
        если он (слот) пустой (без фильтра).
        Также здесь следует проверять, что в первый слот можно установить только объекты класса Mechanical,
        во второй - объекты класса Aragon и в третий - объекты класса Calcium. Иначе слот должен оставаться пустым.
        :param slot_num:
        :param filter:
        :return:
        """
        # повторное добавление в занятый слот - невозможно
        if self.verify_filter(slot_num, filter) and self.filters_installed[slot_num] is None:
            self.filters_installed[slot_num] = filter

    def remove_filter(self, slot_num):
        if self.verify_filter(slot_num):
            self.filters_installed[slot_num] = None

    def get_filters(self):
        installed_filters = self.filters_installed
        return tuple(v for (k, v) in installed_filters.items())

    def water_on(self):
        """
        True, если выполнены условия:
        - все три фильтра установлены в слотах;
        - все фильтры работают в пределах срока службы
        (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])
        :return: True | False
        """
        return all(self.filters_installed.values()) and \
               all([0 <= time.time() - x.date <= self.MAX_DATE_FILTER
                    for x in self.filters_installed.values()])


# Далее - для самопроверки:


if __name__ == '__main__':
    my_water = GeyserClassic()
    my_water.add_filter(1, Mechanical(time.time()))
    my_water.add_filter(2, Aragon(time.time()))
    print(*[(k, v) for (k, v) in my_water.__dict__.items()], sep='\n')
    w = my_water.water_on()  # False
    print(w)
    my_water.add_filter(3, Calcium(time.time()))
    w_2 = my_water.water_on()  # True
    print(w_2)
    f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
    print("Установленные фильтры:")
    print(f1, f2, f3, sep='\n')
    time.sleep(1.5)
    print("\nПробуем переприсвоить значение даты для одного из фильтров:")
    date_before = f1.date
    print(*[(k, v) for (k, v) in f1.__dict__.items()], sep='\n')
    print(f"Значение даты в  объекте  <{f1}>  ДО ПОПЫТКИ изменения даты = <{date_before}>")
    f1.date = time.time()
    date_after = f1.date
    print(f"Значение даты в объекте <{f1}> ПОСЛЕ ПОПЫТКИ изменения даты = <{date_after}>")
    print(*[(k, v) for (k, v) in f1.__dict__.items()], sep='\n')
    print(f"Даты - равны? <{date_before == date_after}>")
    my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
    my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
    print(*[(k, v) for (k, v) in my_water.__dict__.items()], sep='\n')
    filters = my_water.get_filters()
    print(filters)

    print("\nЕще один фильтр:")
    geizer_1 = GeyserClassic()
    geizer_1.add_filter(1, Mechanical(time.time()))
    geizer_1.add_filter(2, Mechanical(time.time()))
    geizer_1.add_filter(3, Calcium(time.time()))
    print(*[(k, v) for (k, v) in geizer_1.__dict__.items()], sep='\n')
    print(geizer_1.water_on())
    slot_num_delete = 1
    print(f"Удаляем фильтр в <{slot_num_delete}>-ом слоте")
    geizer_1.remove_filter(slot_num=slot_num_delete)
    print(*[(k, v) for (k, v) in geizer_1.__dict__.items()], sep='\n')

    print("Пробуем создать фильтр без даты:")
    f_1_test = Mechanical(-0.1)
    print(*[(k, v) for (k, v) in f_1_test.__dict__.items()], sep='\n')
    f_1_test.date = time.time()
    print(f_1_test.date)
    print(f_1_test.__getattr__("date"))
    print(f_1_test.__getattr__("aefsdgg"))
    print(f_1_test.__getattr__("filter_installed"))
    print(*[(k, v) for (k, v) in f_1_test.__dict__.items()], sep='\n')
