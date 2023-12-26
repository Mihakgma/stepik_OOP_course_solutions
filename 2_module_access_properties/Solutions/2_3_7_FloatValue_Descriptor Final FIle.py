"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/xHINhSQJh5c

Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения.
При записи вещественного числа должна выполняться проверка на вещественный тип данных.
Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")
Объявите класс Cell, в котором создается объект value дескриптора FloatValue.
А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)
Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell,
работать с вещественными числами через объект value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3.
Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

P.S. На экран в программе выводить ничего не нужно.
"""


class FloatValue:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        # print(f"__set__: {self.name} = {value}")
        instance.__dict__[self.name] = value


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell() for m in range(M)] for n in range(N)]

    def fill_table(self):
        n = self.N
        m = self.M
        df_shadow = []
        count = 1
        for i, sublist in enumerate(self.cells):
            # print(i, sublist)
            df_shadow.append([setattr(cell, 'value', float(digit)) for (digit, cell) in
                              zip(range(count, len(sublist) + count), sublist)])
            count += len(sublist)
        return df_shadow

    def print_cell_values(self):
        df = self.cells
        print(*[[cell.value for cell in row] for row in df], sep='\n')


if __name__ == '__main__':
    numbers = [float(i) for i in range(1, 16)]
    table = TableSheet(N=5, M=3)
    # table.print_cell_values()
    # print(*[row for row in table.cells], sep='\n')
    table.fill_table()
    # table.print_cell_values()

    # print(*[(k, v) for (k, v) in table.__dict__.items()], sep='\n')
    # [setattr(cell, 'value', digit) for (cell, digit) in zip(table.cells, numbers)]
    # print(*[cell.value for cell in table.cells], sep='\n')
    # print(*[cell.__dict__ for cell in table.cells], sep='\n')
    # print(*[(k, v) for (k, v) in table.__dict__.items()], sep='\n')
