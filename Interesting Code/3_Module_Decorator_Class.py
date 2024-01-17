class Decorator:
    def __init__(self, func):
        self.__func = func

    def __call__(self, x, y=1):
        print(f'y = {y}')
        return self.__func(x) + y


@Decorator
def my_func(x):
    return x


if __name__ == '__main__':
    print(type(my_func))
    a = my_func(10)  # Попробуйте добавить второй аргумент
    print(a)
