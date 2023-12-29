"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/zCD5_APRzes

Подвиг 7. Объявите класс ValidateString для проверки корректности переданной строки.
Объекты этого класса создаются командой:

validate = ValidateString(min_length=3, max_length=100)
где min_length - минимальное число символов в строке; max_length - максимальное число символов в строке.
В классе ValidateString должен быть реализован метод:

validate(self, string) - возвращает True, если string является строкой (тип str) и длина строки в пределах
[min_length; max_length]. Иначе возвращается False.

Объявите дескриптор данных StringValue для работы со строками, объекты которого создаются командой:

st = StringValue(validator=ValidateString(min_length, max_length))
При каждом присвоении значения объекту st должен вызываться валидатор (объект класса ValidateString)
и с помощью метода validate() проверяться корректность присваиваемых данных. Если данные некорректны,
то присвоение не выполняется (игнорируется).

Объявите класс RegisterForm с тремя объектами дескриптора StringValue:

login = StringValue(...) - для ввода логина;
password = StringValue(...)  - для ввода пароля;
email = StringValue(...)  - для ввода Email.

Объекты класса RegisterForm создаются командой:

form = RegisterForm(логин, пароль, email)
где логин, пароль, email - начальные значения логина, пароля и Email.
В классе RegisterForm также должны быть объявлены методы:

get_fields() - возвращает список из значений полей в порядке [login, password, email];
show() - выводит в консоль многострочную строку в формате:

<form>
Логин: <login>
Пароль: <password>
Email: <email>
</form>

P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""


class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) is str and self.min_length <= len(string) <= self.max_length


class StringValue:

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.name] = value


class RegisterForm:
    login, password, email = [StringValue(validator=ValidateString()) for i in range(3)]

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'''<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>''')


if __name__ == '__main__':
    form = RegisterForm("логин", 'пароль', "почта")
    form.show()
    print(*[(k, v) for (k, v) in form.__dict__.items()], sep='\n')
    res = form.get_fields()
    print(res)
    print("Проверка с помощью списка значений для пароля!")
    test_passwords = [1234, 'sdfnsdf322', 5345, 'df', '_']
    counter = 0
    for val in test_passwords:
        counter += 1
        print(counter)
        is_valid = ['НЕВАЛИДНОЕ', 'ВАЛИДНОЕ'][ValidateString().validate(string=val)]
        print(f"Попытались поменять пароль на <{is_valid}> значение: <{val}>")
        form.password = val
        form.show()
