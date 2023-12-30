"""
НЕпонятно, почему переменные созданные в процессе вызова функций / методов классов
перемещаются в текущую область видимости, а не уничтожаются после выполнения
метода/ функции сборщиком мусора???
"""

class SomeClass:
    def do_something(self, *args) -> object:
        pass


if __name__ == '__main__':
    local_vars_before = dir()
    try:
        print(n + '_')
    except NameError:
        print('Переменная не была объявлена!')
    # print(*local_vars_before, sep='\n')
    some_obj = SomeClass()
    some_obj.do_something((n := input('Введите строку для обмена последнего и первого символов в ней:\n'))[-1],
                          n[1:-1],
                          n[0])
    some_obj.x = 30
    local_vars_after = dir()
    variable_visible = ['Local variables list has been changed!', 'Local variables list has NOT been changed!']
    print(variable_visible[local_vars_before == local_vars_after])
    # Действительно, в текущей области видимости появилась новая переменная, заданная в ...
    print(n + '2')
    print(some_obj.__dict__)
    # print(*local_vars_after, sep='\n')