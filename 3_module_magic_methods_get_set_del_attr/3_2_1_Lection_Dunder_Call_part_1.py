class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter


if __name__ == '__main__':
    # когда указываем круглые скобочки после наименования класса,
    # то мы тем самым вызываем магический метод __call__ класса...
    # т.е. благодаря методу __call__ мы класс можем вызывать как функцию,
    # а вот экземпляр класса мы таким образом вызывать уже не можем!!!
    # НЕ МОЖЕМ ЕГО ВЫЗЫВАТЬ ДО ТОХ ПОР, ПОКА НЕ ПЕРЕОПРЕДЕЛИЛИ маг. метод __call__!!!
    # классы, которые таким образом себя ведут, называются ФУНКТОРАМИ!!!
    c = Counter()
    # c()  # (если __call__ явно не переопределен, то возникнет ошибка) TypeError: 'Counter' object is not callable
    for i in range(5):
        print(c())
    print(c.__dict__)
    c2 = Counter()
    c2(step=3)
    print(c2.__dict__)
