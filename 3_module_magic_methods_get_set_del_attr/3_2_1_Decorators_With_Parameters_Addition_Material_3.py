"""
https://www.youtube.com/watch?v=bl_CnIVpWmQ
"""
# Декораторы функций с параметрами
# Правильное описание функции-декораторв, которая бы была способна принимать дополнительные параметры...
from functools import wraps
import math


def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__

        return wrapper
    return func_decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    """
    Функция для вычисления производной синуса переменной x
    :param x:
    :return:
    """
    return math.sin(x)


if __name__ == '__main__':
    df = sin_df(math.pi / 3)
    print(df)
    print(sin_df.__name__, sin_df.__doc__)
