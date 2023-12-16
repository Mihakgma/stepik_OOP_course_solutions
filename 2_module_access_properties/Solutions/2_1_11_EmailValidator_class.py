"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HPgJtLb2NV8

Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса:
при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""
from random import choice as rnd_choice
from random import randint as rnd_randint


class EmailValidator:
    RIGHT_SYMBOLS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"
    NOT_RIGHT_SYMBOLS = " *()-+=&?#№$%^!';,[]{}"
    EMAIL_LEN_MIN = 5
    EMAIL_LEN_MAX = 35

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def get_test_email(cls, valid=False):
        if valid:
            symbols = cls.RIGHT_SYMBOLS
        else:
            symbols = cls.RIGHT_SYMBOLS + cls.NOT_RIGHT_SYMBOLS
        email_len = rnd_randint(cls.EMAIL_LEN_MIN, cls.EMAIL_LEN_MAX)
        email_test = ''.join([rnd_choice(symbols) for i in range(email_len)])
        return email_test

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if any([s not in cls.RIGHT_SYMBOLS for s in email]):
            return False
        if email.count("@") != 1 or ".." in email:
            return False
        split_email = email.split("@")
        if len(split_email[0]) > 100 or len(split_email[1]) > 50 or "." not in split_email[1]:
            return False
        return True

    @classmethod
    def get_random_email(cls):
        while True:
            test_email = cls.get_test_email(valid=True)
            if cls.check_email(test_email):
                return test_email


# Далее - для самопроверки!
if __name__ == '__main__':
    validator_1 = EmailValidator()
    print(validator_1)
    res_1 = EmailValidator.check_email("sc_lib@list.ru")  # True
    res_2 = EmailValidator.check_email("sc_lib@list_ru")
    res_3 = EmailValidator.check_email(4324)
    res_4 = EmailValidator.check_email("sc_@lib@list_ru")
    res_5 = EmailValidator.check_email("sc_lib@list..ru")
    res_6 = EmailValidator.check_email("!sc_lib@list.ru")
    print(res_1, res_2, res_3, res_4, res_5, res_6)
    print()

    emails_number = 10000
    results_dict = {}
    for i in range(emails_number):
        check_email = EmailValidator.get_test_email()
        results_dict[check_email] = EmailValidator.check_email(email=check_email)
    print(*[f'Is <{key}> correct email: <{val}>'
            for (key, val) in results_dict.items() if val], sep='\n')
