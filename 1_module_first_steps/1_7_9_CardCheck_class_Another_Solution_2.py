"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9766M0dS1qc

Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах.
Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX,
где X - любая цифра (от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True,
если имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами.
Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""
import timeit  # для замеров времени исполенния кода!!!
from pandas import Series as pd_Series
from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        """проверяет строку с номером карты и возвращает булево значение True,
        если номер в верном формате и False - в противном случае. Формат номера,
        следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)."""
        figures = number.split('-')
        return len(figures) == 4 and all([len(d) == 4 and d.isdigit() for d in figures])

    @classmethod
    def check_name(cls, name):
        """проверяет строку name с именем пользователя карты.
        Возвращает булево значение True, если имя записано верно
        и False - в противном случае.
        Формат имени: два слова (имя и фамилия) через пробел,
        записанные заглавными латинскими символами и цифрами.
        Например, SERGEI BALAKIREV."""
        fi = name.split()
        return all([c in cls.CHARS_FOR_NAME + ' ' for c in name]) and len(fi) == 2


if __name__ == '__main__':
    is_number = CardCheck.check_card_number("1234-5678-9012-0000")
    is_name = CardCheck.check_name("SERGEI BALAKIREV")

    # ДАЛЕЕ - ДЛЯ ПРОВЕРКИ!!!
    elapsed_time = []
    iterations = 10000
    numbers = [
        "1234-5678-9012-0000",
        "sdf3-a431-4232-0000",
        "1111-2222-3333-4444",
        "4234-9999-1111-32g9",
        "sjdd-sfls-sdfs-fd92"
    ]
    names = [
        "SERGEI BALAKIREV",
        "mr SERGEI BALAKIREV",
        "SERGEI BALAKIREV CHI-FU",
        "MIKHAIL DOROSHKO",
        "ALEXANDR ONOPENKO chap"
    ]
    for i in range(iterations):
        start = timeit.default_timer()
        for num, name in zip(numbers, names):
            is_number = CardCheck.check_card_number(number=num)
            is_name = CardCheck.check_name(name=name)
            print(is_number, is_name)

        stop = timeit.default_timer()
        # print('Time: ', stop - start)
        elapsed_time.append(stop - start)
    print(pd_Series(elapsed_time).describe())
