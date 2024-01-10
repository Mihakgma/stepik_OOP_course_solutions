"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/fiYiJWXv-5I

Подвиг 2. Объявите класс RandomPassword для генерации случайных паролей.
Объекты этого класса должны создаваться командой:

rnd = RandomPassword(psw_chars, min_length, max_length)
где psw_chars - строка из разрешенных в пароле символов; min_length,
max_length - минимальная и максимальная длина генерируемых паролей.

Непосредственная генерация одного пароля должна выполняться командой:

psw = rnd()
где psw - ссылка на строку длиной в диапазоне [min_length;
max_length] из случайно выбранных символов строки psw_chars.

С помощью генератора списка (list comprehension) создайте список lst_pass
из трех сгенерированных паролей объектом rnd класса RandomPassword, созданного с параметрами:

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
P.S. Выводить на экран ничего не нужно, только создать список из паролей.

P.P.S. Дополнительное домашнее задание: попробуйте реализовать этот же функционал с использованием замыканий функций.
"""
from random import randint, choice


# доп задание - через замыкания
def random_password(password_chars, min_length, max_length):
    def wrapper():
        length = randint(min_length, max_length)
        password = ''.join([choice(password_chars) for _ in range(length)])
        return password

    return wrapper


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def generate_password(self):
        chars = self.psw_chars
        min_length = self.min_length
        max_length = self.max_length
        password_length = randint(min_length, max_length)
        return ''.join([choice(chars) for i in range(password_length)])

    def __call__(self, *args, **kwargs):
        return self.generate_password()


if __name__ == '__main__':
    passwords_number = 3
    p = RandomPassword(min_length=5,
                       max_length=20,
                       psw_chars="qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*")
    lst_pass = [p() for i in range(passwords_number)]
    # Далее - для самопроверки:
    print(*lst_pass, sep='\n')
    pswd = random_password("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*",
                           5, 20)
    print(pswd())
