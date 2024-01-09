"""
https://www.youtube.com/watch?v=v0qZPplzwUQ&t=611s
"""
# Декораторы. Способы применения.
import time


def func_decorator(func):
    """
    Универсальный декоратор!!!
    :param func: оборчиваемая в декоратор функция
    :return: результат выполнения обернутой функции
    """
    def wrapper(*args, **kwargs):
        # print("----------- что-то делаем перед вызовом функции -----------")
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        # print("----------- что-то делаем после  вызова функции -----------")
        dt = et - st
        print(f"Время работы: {dt} сек.")
        return res

    return wrapper


def some_func(message):
    print(f"Внимание!!! <{message}>")
    return True


@func_decorator
def get_nod(a, b):
    """
    Медленный алгоритм Евклида
    :param a:
    :param b:
    :return:
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@func_decorator
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    # пример "обертывания" функции в декоратор
    f = func_decorator(func=some_func)
    r = f("Python ForEver!!!")
    print(r)

    # get_nod = func_decorator(get_nod)
    # get_fast_nod = func_decorator(get_fast_nod)

    res = get_nod(2, 1000000)
    res2 = get_fast_nod(2, 1000000)
    print(res, res2)
