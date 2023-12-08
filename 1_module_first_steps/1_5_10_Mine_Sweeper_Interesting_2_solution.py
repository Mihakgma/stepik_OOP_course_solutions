"""
Если i = 0, а j = 2. То i действительно соберёт срез self.pole[0 : 2] - то есть две строки 0 и 1.
А j соберёт срез из столбцов этих строк [1:4].
По условию, которое прописано для среза у j: j - 1 if j - 1 > 0 else 0: j + 2
Так и получается, что мы проверим все необходимые клетки)
"""


from random import randint


class Cell:

    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:

    def __init__(self, N, M):
        self.size = N
        self.mines = M
        self.pole = []
        self.init()

    def init(self):
        N = self.size
        M = self.mines
        self.pole = [[Cell(0, False) for _ in range(N)] for _ in range(N)]
        self._place_mines(M, N)
        self._count_mines(N)

    def _place_mines(self, M, N):
        while M > 0:
            tmp_row = randint(0, N - 1)
            tmp_coll = randint(0, N - 1)
            if not self.pole[tmp_row][tmp_coll].mine:
                self.pole[tmp_row][tmp_coll].mine = True
                M -= 1

    def _count_mines(self, N):
        for i in range(N):
            for j in range(N):
                self.pole[i][j].around_mines = sum([cell.mine
                                                    for row in self.pole[i - 1 if i - 1 > 0 else 0:i + 2]
                                                    for cell in row[j - 1 if j - 1 > 0 else 0: j + 2]])

    def show(self):
        [print(*[i.around_mines if i.fl_open else '#' for i in row]) for row in self.pole]




if __name__ == '__main__':
    pole_game = GamePole(10, 12)
    # pole_game.show()
