class Money:
    def __init__(self):
        self.__money = 0

    def set_money(self, value):
        self.__money = value

    def get_money(self):
        return self.__money

    money = property(get_money, set_money)


if __name__ == '__main__':
    m = Money()
    m.money = 10
    print(m.__dict__)
    res = m.money
    print(res)
    m.__dict__['money'] = 100
    res = m.money
    print(res)
    