"""
https://www.youtube.com/watch?v=v0qZPplzwUQ&t=611s
"""
# Декораторы. Способы применения.


def func_decorator(func):
    """
    Универсальный декоратор!!!
    :param func: оборчиваемая в декоратор функция
    :return: результат выполнения обернутой функции
    """
    def wrapper(*args, **kwargs):
        print("----------- что-то делаем перед вызовом функции -----------")
        res = func(*args, **kwargs)
        print("----------- что-то делаем после  вызова функции -----------")
        return res

    return wrapper


def some_func(message):
    print(f"Внимание!!! <{message}>")
    return True


if __name__ == '__main__':
    # пример "обертывания" функции в декоратор
    f = func_decorator(func=some_func)
    r = f("Python ForEver!!!")
    print(r)
