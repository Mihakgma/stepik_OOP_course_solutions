"""
Испытание свойствами и методами

Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/26pwwOu_-d0

Время первого испытания. Представьте, что вы получили задание от заказчика.
Вас просят реализовать простую имитацию локальной сети,
состоящую из набора серверов, соединенных между собой через роутер.

Каждый сервер может отправлять пакет любому другому серверу сети. Д
ля этого у каждого есть свой уникальный IP-адрес. Для простоты - это просто целое (натуральное) число
от 1 и до N, где N - общее число серверов. Алгоритм следующий.
Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3.
Для этого, он сначала отправляет пакет роутеру, а уже тот,
смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).

Для реализации этой схемы программе предлагается объявить три класса:

Server - для описания работы серверов в сети;
Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
Data - для описания пакета информации.

Серверы будут создаваться командой:

sv = Server()

При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически
при создании нового экземпляра класса Server.

Далее, роутер должен создаваться аналогичной командой:

router = Router()

А, пакеты данных, командой:

data = Data(строка с данными, IP-адрес назначения)

Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:

link(server) - для присоединения сервера server (объекта класса Server) к роутеру
(для простоты, каждый сервер соединен только с одним роутером);
unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
(после отправки буфер должен очищаться).

И одно обязательное локальное свойство (могут быть и другие свойства):

buffer - список для хранения принятых от серверов пакетов (объектов класса Data).

Класс Server должен содержать свой набор методов:

send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
(пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
и очищает входной буфер;
get_ip() - возвращает свой IP-адрес.

Соответственно в объектах класса Server должны быть локальные свойства:

buffer - список принятых пакетов (объекты класса Data, изначально пустой);
ip - IP-адрес текущего сервера.

Наконец, объекты класса Data должны содержать два следующих локальных свойства:

data - передаваемые данные (строка);
ip - IP-адрес назначения.

Пример использования этих классов (эти строчки в программе писать не нужно):

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

Ваша задача реализовать классы Router, Server и Data в соответствии с приведенным техническим заданием (ТЗ).
Что-либо выводить на экран не нужно.
"""


class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    SERVERS = dict()

    def __new__(cls, *args, **kwargs):
        new_server_ip = len(cls.SERVERS) + 1
        new_server_obj = super().__new__(cls)
        cls.SERVERS[new_server_ip] = new_server_obj
        return new_server_obj

    def __init__(self):
        self.data = []
        self.ip = max([key for key in self.SERVERS])

    @classmethod
    def send_data(cls, data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer);
        """
        rt = Router()
        rt.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер;
        """
        return self.data

    def append_data(self, data: str):
        self.data.append(data)

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    __instance = None
    LINKED_SERVERS = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        # для сохранения списка IP-адресов присоединенных серверов
        self.linked_servers = []
        self.buffer = []

    @classmethod
    def link_cls(cls, ip):
        cls.LINKED_SERVERS.append(ip)

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        self.linked_servers.append(server.ip)
        self.link_cls(server.ip)

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        self.linked_servers.remove(server.ip)

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        sv_temp = Server()
        [sv_temp.SERVERS[obj.ip].append_data(data=obj) for obj in self.buffer if obj.ip in self.linked_servers]
        self.buffer = []
        # удяляем временный сервер
        del sv_temp
        # [sv_temp.send_data(obj) for ip, obj in self.RECEIVER_IP_DATA.items() if ip in self.linked_servers]


class Data:
    """
    объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


if __name__ == '__main__':
    # далее - для проверки работоспособности программы
    sv, sv_1 = Server(), Server()
    print(sv.__dict__, sv_1.__dict__)
    router = Router()
    router.link(sv)
    router.link(sv_1)
    print(router.__dict__)
    sv.send_data(data=Data('Привет от первого сервера!', sv_1.get_ip()))
    print(router.__dict__)
    router.send_data()
    msg_list_sv_1 = sv_1.get_data()
    print(msg_list_sv_1)
    print(sv.__dict__, sv_1.__dict__)
