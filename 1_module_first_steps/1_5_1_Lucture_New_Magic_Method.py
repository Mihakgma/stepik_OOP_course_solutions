"""
Lecture:
https://www.youtube.com/watch?v=-J3Ou8-8vVk
"""


class Test:
    def __init__(self):
        self.name = self

    def __del__(self):
        print(f'Зашли в удаление объекта {self}')
        del self

if __name__ == '__main__':
    exists = ['Существует', 'Не существует']
    test = Test()
    test2 = test
    print('До удаления')
    print(*[var for var in locals()], sep='\n')
    print()
    test.__del__()
    del test
    print('После удаления')
    print(*[var for var in locals()], sep='\n')
    print()
    print(f'Имя <{test2.name}>: {exists[test2.name is None]}')
    print('Явным образом удаляем второй созданный объект!')
    # del test2
    test2.__del__()
    # print(f'Имя <{test2.name}>: {exists[test2.name is None]}')
    print(f'Имя <{test2.name}>: {exists[test2.name not in locals()]}')
    print(*[var for var in locals()], sep='\n')
    print()
    del test2
    try:
        print(f'Имя <{test2.name}>: {exists[test2.name not in locals()]}')
    except BaseException as e:
        print(f'Возникла ошибка <{e}> при попытке поиска объекта класса <{Test}>')

    print(*[var for var in locals()], sep='\n')
    print()
