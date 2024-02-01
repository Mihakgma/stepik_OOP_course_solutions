import sys


class Thing:
    SEQ_ID = (i for i in range(1, sys.maxsize))

    def __init__(self, name, price):
        self.id = self.get_id()
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    @classmethod
    def get_id(cls):
        return next(cls.SEQ_ID)


class Table(Thing):
    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


if __name__ == '__main__':
    table = Table("Круглый", 1024, 812.55, (700, 750, 700))
    book = ElBook("Python ООП", 2000, 2048, 'pdf')
    print("метод get_data() - не прописан!")
    # print(*table.get_data())
    # print(*book.get_data())
