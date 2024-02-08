"""
Подвиг 8 (на повторение). Объявите класс SoftList, который наследуется от стандартного класса list.
В классе SoftList следует объявить необходимые магические методы так,
чтобы при обращении к несуществующему элементу (по индексу) возвращалось значение False (а не исключение Out of Range).
Например:

sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
sl[-7] # False
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.
"""


class SoftList(list):
    def __getitem__(self, *args):
        index = args[0]
        try:
            res = super().__getitem__(index)
        except IndexError:
            res = False
        return res


if __name__ == '__main__':
    sl = SoftList("python")
    sl[0]  # 'p'
    sl[-1]  # 'n'
    sl[6]  # False
    sl[-7]  # False
    for i in [0, -1, 6, -7]:
        print(sl[i])
