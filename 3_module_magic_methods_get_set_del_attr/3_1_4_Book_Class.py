"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/lI99OdJt71w

Подвиг 3. Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:

book = Book()
book = Book(название, автор, число страниц, год издания)
В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:

title - заголовок книги (строка, по умолчанию пустая строка);
author - автор книги (строка, по умолчанию пустая строка);
pages - число страниц (целое число, по умолчанию 0);
year - год издания (целое число, по умолчанию 0).

Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным свойствам
title, author, pages и year. Если типы не соответствуют локальному атрибуту
(например, title должна ссылаться на строку, а pages - на целое число), то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
Создайте в программе объект book класса Book для книги:

автор: Сергей Балакирев
заголовок: Python ООП
pages: 123
year: 2022

P.S. На экран ничего выводить не нужно.
"""


class Book:
    attributes_str = ["title", "author"]
    attributes_natural_digit = ["pages", "year"]

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if type(value) == str and key in self.attributes_str:
            pass
        elif type(value) == int and key in self.attributes_natural_digit and value >= 0:
            pass
        else:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)
        

if __name__ == '__main__':
    book = Book(author="Сергей Балакирев",
                title="Python ООП",
                pages=123,
                year=2022)
    # Далее - для сомопроверки:
    print(book.__dict__)
    book_2 = Book(title=555)
