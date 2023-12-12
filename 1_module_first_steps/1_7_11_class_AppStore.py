"""
1.7 Методы класса (classmethod) и статические методы (staticmethod)
10 из 12 шагов пройдено
16 из 22 баллов  получено
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Y4Hvpg4FuKs

Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS.
В этом классе должны быть реализованы следующие методы:

add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app
(устанавливает локальное свойство blocked объекта app в значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным именем.
Каждый объект класса Application должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.

P.S. В программе нужно только объявить классы с указанным функционалом.
"""


class AppStore:
    """Объявите класс AppStore - интернет-магазин приложений для устройств
    под iOS. В этом классе должны быть реализованы следующие методы:
    """
    APPLICATIONS = []

    @classmethod
    def add_application(cls, app):
        """добавление нового приложения app в магазин
        """
        if app.blocked:
            pass
        else:
            cls.APPLICATIONS.append(app)

    @classmethod
    def remove_application(cls, app):
        """удаление приложения app из магазина
        """
        cls.APPLICATIONS.remove(app)

    @staticmethod
    def block_application(app):
        """блокировка приложения app (устанавливает локальное
        свойство blocked объекта app в значение True)
        """
        app.blocked = True

    @classmethod
    def total_apps(cls):
        """возвращает общее число приложений в магазине
        """
        return len(cls.APPLICATIONS)


class Application:
    """Здесь Application - класс, описывающий добавляемое приложение
    с указанным именем. Каждый объект класса Application должен содержать
    локальные свойства:
    name - наименование приложения (строка);
    blocked - булево значение (True - приложение заблокировано;
    False - не заблокировано, изначально False).
    """
    def __init__(self, name: str, blocked: bool=False):
        self.name = name
        self.blocked = blocked


if __name__ == '__main__':
    # далее - для проверки работоспособности программы
    store = AppStore()
    app_youtube = Application("Youtube")
    store.add_application(app_youtube)
    print(*[(key, value) for (key, value) in AppStore.__dict__.items()], sep='\n')
    store.remove_application(app_youtube)
    print(*[(key, value) for (key, value) in AppStore.__dict__.items()], sep='\n')
    app_twitter = Application('Tweeter')
    print(app_twitter.__dict__)
    AppStore().block_application(app=app_twitter)
    print(app_twitter.__dict__)
    store.add_application(app=app_twitter)
    print(*[(key, value) for (key, value) in AppStore.__dict__.items()], sep='\n')
    app_blablacar = Application('BlaBlaCar')
    store.add_application(app=app_blablacar)
    print(*[(key, value) for (key, value) in AppStore.__dict__.items()], sep='\n')
