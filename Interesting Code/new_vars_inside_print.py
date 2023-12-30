if __name__ == '__main__':
    local_vars_before = dir()
    try:
        print(n + '_')
    except NameError:
        print('Переменная не была объявлена!')
    # print(*local_vars_before, sep='\n')
    print((n := input('Введите строку для обмена последнего и первого символов в ней:\n'))[-1],
          n[1:-1],
          n[0],
          sep='')
    local_vars_after = dir()
    variable_visible = ['Local variables list has been changed!', 'Local variables list has NOT been changed!']
    print(variable_visible[local_vars_before == local_vars_after])
    # Действительно, в текущей области видимости появилась новая переменная, заданная в print-е
    print(n + '2')
    # print(*local_vars_after, sep='\n')
