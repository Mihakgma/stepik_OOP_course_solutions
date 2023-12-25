"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/TMPPmryMKD0

Подвиг 10 (на закрепление). Вы создаете телефонную записную книжку. Она определяется классом PhoneBook.
Объекты этого класса создаются командой:

p = PhoneBook()
А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class PhoneNumber:
    NUMBER_DEFAULT = 00000000000
    FIO_DEFAULT = ''

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

    def get_number(self):
        return self.number

    def set_number(self, number):
        setattr(self, 'number',
                [self.NUMBER_DEFAULT, number][self.is_phone_number(number)])

    def get_fio(self):
        return self.fio

    def set_fio(self, fio):
        setattr(self, 'fio',
                [self.FIO_DEFAULT, fio][self.is_fio(fio)])

    @classmethod
    def is_phone_number(cls, number):
        return type(number) is int and str(number) == 11

    @classmethod
    def is_fio(cls, fio):
        return type(fio) is str


class PhoneBook:
    def __init__(self):
        self.phone_list = []

    def add_phone(self, phone: PhoneNumber):
        self.phone_list.append(phone)

    def remove_phone(self, indx):
        self.phone_list.pop(indx)

    def get_phone_list(self):
        return [contact.number for contact in self.phone_list]

    def get_fio_list(self):
        return self.phone_list


# Далее - для проверки!
if __name__ == '__main__':
    p = PhoneBook()
    p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
    p.add_phone(PhoneNumber(21345678901, "Панда"))
    phones = p.get_phone_list()
    print(*phones, sep='\n')
    contacts = p.get_fio_list()
    print(*contacts, sep='\n')
    p.remove_phone(indx=1)
    print(*[(k, v) for (k, v) in p.__dict__.items()], sep='\n')
    test_contact = PhoneNumber('sdfnjsdf', 8978)
    print(*[(k, v) for (k, v) in test_contact.__dict__.items()], sep='\n')
