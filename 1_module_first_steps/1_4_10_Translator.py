"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/butyKEUntK0

Подвиг 10. Дан класс Translator (для перевода с английского на русский), в котором объявлены три метода:

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add

    def remove(self, eng):
        # здесь продолжайте метод remove

    def translate(self, eng):
        # здесь продолжайте метод translate
В объекте этого класса должны локально (в атрибуте tr) храниться связки между английским и русскими словами
в виде следующего словаря:

{'<английское слово>': [<одно или несколько русских слов>], ...}

Методы должны делать следующее:

add(self, eng, rus) - для добавления в словарь новой связки английского и русского слова (если английское слово
уже существует, то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать);
если связка eng-rus уже существует, то второй раз ее добавлять не нужно,
например:  add('go', 'идти'), add('go', 'идти');
remove(self, eng) - для удаления из словаря связки по указанному английскому слову;
translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов,
 соответствующих переводу английского слова, даже если в списке всего одно слово).

Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator,
т.е. связки хранить локально внутри экземпляров классов класса Translator, используя коллекцию-словарь.
(Хранить связки непосредственно в коллекции __dict__ не нужно!)

Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:

tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко

Затем методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go.
Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:

Вывод в формате: идти ехать ходить
"""
import sys


class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        # здесь продолжайте метод remove
        d = self.tr
        try:
            del d[eng]
            self.tr = d
        except:
            print(f'Word <{eng}> is not in dictionary!')

    def translate(self, eng):
        # здесь продолжайте метод translate
        return self.tr[eng]


# здесь создавайте объект класса Translator
if __name__ == '__main__':
    lst_in = list(map((str.strip), sys.stdin.readlines()))  # считывание списка строк из входного потока
    lst_in = [i.split(' - ') for i in lst_in]
    # print(lst_in)
    tr = Translator()
    [tr.add(i[0], i[1]) for i in lst_in]
    # tr.add("tree", "дерево")
    # tr.add("car", "машина")
    # tr.add("car", "автомобиль")
    # tr.add("leaf", "лист")
    # tr.add("river", "река")
    # tr.add("go", "идти")
    # tr.add("go", "ехать")
    # tr.add("go", "ходить")
    # tr.add("milk", "молоко")
    key_2del = 'pig'
    tr.remove(key_2del)
    print(key_2del in tr.__dict__)
    print('\n'.join([i for i in tr.__dict__]))
