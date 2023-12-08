# здесь пишется программа
from random import shuffle as rnd_shiffle
# from random import randint as rnd_randint


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
    # field_lst = []
    def __init__(self, N: int, M: int):
        cells_total = N * N
        self.cells_total = cells_total
        self.field_lst = []
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
        self.init()

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
                # cell_obj.set_fl_open(True)
                out_symbol = cell_obj.reveal_obj()
                new_row.append(out_symbol)
            print(*new_row)


    def init(self):
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
    pole_game = GamePole(N=10, M=12)
    pole_game.show()
    print(hasattr(GamePole, 'show'))
    print(isinstance(pole_game, GamePole))
    print(hasattr(GamePole, 'init'))
