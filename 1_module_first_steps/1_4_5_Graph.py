"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/XNbphw3bYAI

Подвиг 5. Объявите класс с именем Graph и методами:

set_data(buffer) - передача набора данных buffer для последующего отображения (buffer - список числовых данных);
draw() - отображение данных (в том же порядке, что и в списке buffer)

и атрибутом:

LIMIT_Y = [0, 10]

Метод set_data() должен формировать локальное свойство buffer объекта класса Graph.
Атрибут buffer должен ссылаться на переданный в метод список.
Метод draw() должен выводить на экран список в виде строки из чисел,
разделенных пробелами и принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).

Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и передайте список:

[10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с соответствующим набором чисел,
записанных через пробел. Например (вывод без кавычек):

"10 0 2 5 7"
"""


class Graph():
    LIMIT_Y = [0, 10]

    def set_data(self, data: list):
        self.data = data

    def draw(self):
        data = self.data
        y_min = self.LIMIT_Y[0]
        y_max = self.LIMIT_Y[1]
        print(' '.join([str(i) for i in data
                        if y_min <= i <= y_max]))

if __name__ == '__main__':
    test_values = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
    graph_1 = Graph()
    graph_1.set_data(data=test_values)
    graph_1.draw()
