class DataBase:
    """
    Лекция:
    https://www.youtube.com/watch?v=-xoT6rntpK0
    Данный класс должен быть реализован с помощью паттерна Singletone,
    т.е. возможно создание лишь одного единственного объекта данного класса!
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'Запись в БД: {data}')

if __name__ == '__main__':
    print(DataBase.__dict__)
    db_1 = DataBase('knyazz', '666', 2379482)
    # принтуем коннект для 1-ого объекта класса
    db_1.connect()
    db_2 = DataBase('motorhead', '999', 2342)
    print(id(db_1), id(db_2))
    print(DataBase.__dict__)
    # оба коннекта принтуют одно и то же, т.к. при инициализации второго объекта он "затер" 1-ый
    db_1.connect()
    db_2.connect()

    # print(db_1. __dict__)