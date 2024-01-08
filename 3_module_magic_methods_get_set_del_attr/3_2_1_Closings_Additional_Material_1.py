"""
https://www.youtube.com/watch?v=sJF7OMNgLUs

48 044 просмотра  29 сент. 2021 г.  Добрый, добрый Python - уроки для начинающих
Обучающий курс: https://stepik.org/course/100707
Что такое замыкания, как они работают и примеры их использования в практике программирования.

Telegram-канал: https://t.me/python_selfedu
"""


def say_name(name):
    def say_goodbye():
        print(f"Don't say me goodbye, {name}!")

    return say_goodbye


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    return step


def strip_string(strip_chars:str=" "):
    def do_strip(string:str):
        return string.strip(strip_chars)
    return do_strip


if __name__ == '__main__':
    # При сохранении функции say_name с разными переменными name
    # создается локальное окружение для функции с индивидуальным значением переменной name!!!
    f = say_name("Mihail")
    f_2 = say_name("Python")
    f()
    f_2()
    # counter
    c1 = counter(33)
    c2 = counter()
    [print(c1(), c2()) for i in range(3)]
    # удаление лишних символов в начале и конце строки!!!
    string_to_strip = " {}|Hello, World!!!?.><||| "
    strip1 = strip_string()
    strip2 = strip_string(" ,?/<>.:;|{}-")
    print(
        strip1(string_to_strip),
        strip2(string_to_strip),
        sep="\n"
    )
