"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/gmjwMakXk0c

Большой подвиг 10. Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)

Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False),
означающая наличие мины в текущей клетке. При этом,
в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие/отсутствие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).

С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)

Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и
все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток
(если клетка не открыта, то отображается символ #; мина отображается символом *;
между клетками при отображении ставить пробел).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init()
для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.

P.S. На экран в программе ничего выводить не нужно.
"""
from random import shuffle as rnd_shiffle
from random import randint as rnd_randint


class Cell:
    def __init__(self, around_mines: int=0, mine: bool=False, fl_open: bool=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open

    def set_around_mines(self, around_mines: int=0):
        self.around_mines = around_mines

    def set_fl_open(self, fl_open: bool):
        self.fl_open = fl_open

    def reveal_obj(self):
        empty_symb = '#'
        bomb_symb = '*'
        around_mines = self.around_mines
        mine = self.mine
        fl_open = self.fl_open
        if not fl_open:
            return empty_symb
        elif mine:  # на ячейку кликнули - мина
            return bomb_symb
        else:  # на ячейку кликнули - количество мин вокруг
            return around_mines


class GamePole:
    field_lst = []
    def __init__(self, N: int, M: int):
        cells_total = N * N
        self.cells_total = cells_total
        self.field_lst = []  # лист с исходным планом (символьное обозначение пустых и клеток с минами) расстановки мин
        self.pole = []  # лист, в котором хранятся объекты класса Cell
        if (cells_total < M or
            N < 1 or M < 0): # количество мин больше, чем клеток поля / отрицательные значения этих параметров
            print('Ошибка инициализации объекта класса GamePole')
            return
        self.N = N
        self.M = M
        field_previous = (['*'] * M) + (['#'] * (self.cells_total - M))
        rnd_shiffle(field_previous)
        self.field_lst = [field_previous[i:i+N]
                          for i in range(0, len(field_previous), N)]

    def show(self):
        field_lst = self.field_lst
        pole = self.pole
        for h in range(len(field_lst)):  # высота поля
            row = field_lst[h]
            pole_row = pole[h]
            # print(*row)
            new_row = []
            for l in range(len(row)):  # ширина поля
                cell_obj = pole_row[l]
                # print(cell_obj)
                cell_obj.set_fl_open(True)
                out_symbol = cell_obj.reveal_obj()
                new_row.append(out_symbol)
            print(*new_row)


    def fill_field(self):
        field_lst = self.field_lst
        # empty_symb = '#'
        bomb_symb = '*'
        pole = []
        for h in range(len(field_lst)):  # высота поля
            row = field_lst[h]
            row_values = []
            for l in range(len(row)):  # ширина поля
                cell = row[l]
                mines_around_total = 0
                if cell == bomb_symb:
                    cell_obj = Cell(mine=True)
                else:
                    cell_obj = Cell()
                # считаем количество мин вокруг текущей ячейки

                try:
                    if (h - 1) > -1:
                        mines_around_total += field_lst[h-1][l] == bomb_symb
                        mines_around_total += field_lst[h-1][l+1] == bomb_symb
                    if  (l - 1) > -1 and (h - 1) > -1:
                        mines_around_total += field_lst[h-1][l-1] == bomb_symb

                except IndexError:
                    pass
                try:
                    if (l - 1) > -1:
                        mines_around_total += row[l-1] == bomb_symb
                except IndexError:
                    pass
                try:
                    mines_around_total += row[l+1] == bomb_symb
                except IndexError:
                    pass
                try:
                    mines_around_total += field_lst[h+1][l] == bomb_symb
                    if (l - 1) > -1:
                        mines_around_total += field_lst[h+1][l-1] == bomb_symb
                    mines_around_total += field_lst[h+1][l+1] == bomb_symb
                except IndexError:
                    pass
                cell_obj.set_around_mines(around_mines=mines_around_total)
                row_values.append(cell_obj)
            pole.append(row_values)
        self.pole = pole
        # print(*[i for i in pole])


if __name__ == '__main__':
    for i in range(3):
        n, m = rnd_randint(3,7), rnd_randint(1,5)
        print(f'n = <{n}>, m = <{m}>')
        gp_test = GamePole(N=n, M=m)
        gp_test.fill_field()
        # print(*gp_test.pole)
        gp_test.show()
