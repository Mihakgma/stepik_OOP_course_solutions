"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ljahVEppmxM

Подвиг 9. Из входного потока читаются строки данных с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода. Первый метод:

insert(self, buffer) - для добавления в конец списка lst_data новых данных из переданного списка строк buffer.
При этом, каждый элемент в списке lst_data должен быть представлен словарем в формате:

{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например, строка "1 Сергей 35 120000" должна быть преобразована в словарь:

{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

и только после этого добавляется в список lst_data. И так для всех строк из переданного списка buffer в метод insert().

Второй метод:

select(self, a, b) - для возвращения нового списка из элементов существующего списка lst_data в диапазоне
индексов [a; b] (включительно) (не id, а индексам списка). Следует иметь в виду,
что граница b может превышать длину списка.

Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей
в коллекции FIELDS.

P. S. Ваша задача только добавить два метода в класс DataBase.

Sample Input:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200

Коммент от С. Петин:

Если работаете в pycharm, то там есть лафхак на ввод данных.
1) создаете какой-нибудь файл, например input.txt
2) записываете в него данные, типа:
1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
3) клик правой кнопкой мыши по вкладке вашего рабочего файла
4) выбираем в раскрывшемся меню пункт:
Modify Run Configuration...
5) Активируем пункт Redirect input from, указываем путь до input.txt, давим ОК
Теперь входные данные будут забираться из input.txt автоматически, экономя ваши время и нервы!)))

"""

import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data: list):
        # print(buffer)
        for elem in data:
            # print(elem)
            current_dict = {}
            for field, value in zip(self.FIELDS, elem.split()):
                current_dict[field] = value
            self.lst_data.append(current_dict)


    def select(self, a: int, b: int):
        lst = self.lst_data
        # print(lst)
        lst_len = len(lst)
        data_selected = [lst[a:], lst[a:b+1]][b + 1 <= lst_len]
        return data_selected


if __name__ == '__main__':
    # print(lst_in)
    print()
    db = DataBase()
    db.insert(lst_in)
    print(db.__dict__)
    result = db.select(a=0, b=1)
    print(*result, sep='\n')
