"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/a3Har3Z_89Q

Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:

gr_1 = Graph(buffer)
где buffer - список из числовых данных (данные для графика). При создании каждого экземпляра класса
должны формироваться следующие локальные свойства:

buffer - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными,
нужно создавать копию переданного списка);
is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика (по умолчанию True);

В этом классе объявите следующие методы:

set_data(self, buffer) - для передачи нового списка данных в текущий график;
show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение:
"Графическое отображение данных: <строка из чисел следующих через пробел>");
show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение:
"Столбчатая диаграмма: <строка из чисел следующих через пробел>");
set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.

Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar()
должны выводить сообщение:

"Отображение данных закрыто"

Прочитайте из входного потока числовые данные с помощью команды:

data_graph = list(map(int, input().split()))
Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(),
затем метод set_show() со значением fl_show = False и вызовите метод show_table().
На экране должны отобразиться две соответствующие строки.

Sample Input:

8 11 10 -32 0 7 18
Sample Output:

Столбчатая диаграмма: 8 11 10 -32 0 7 18
Отображение данных закрыто
"""


class Graph:

    def __init__(self, data: list, is_show: bool=True):
        self.is_show = is_show
        self.data = data.copy()

    def set_data(self, data: list):
        """
        :param data: новый список данных в текущий объект-график
        :return:
        """
        self.data = data.copy()

    def show_table(self):
        is_show = self.is_show
        if not is_show:
            print("Отображение данных закрыто")
        else:
            data = self.data
            print(*data)

    def show_graph(self):
        is_show = self.is_show
        if not is_show:
            print("Отображение данных закрыто")
        else:
            data = self.data
            message = "Графическое отображение данных:"
            print(message, *data)

    def show_bar(self):
        is_show = self.is_show
        if not is_show:
            print("Отображение данных закрыто")
        else:
            data = self.data
            message = "Столбчатая диаграмма:"
            print(message, *data)

    def set_show(self, fl_show: bool):
        setattr(self, 'is_show', fl_show)


if __name__ == '__main__':
    # далее - для проверки
    test_numbers = [1, 2, 3, 54, -12, 0, 2321, 999]
    gr_1 = Graph(data=test_numbers, is_show=True)
    gr_1.show_table()
    gr_1.show_graph()
    gr_1.set_show(fl_show=False)
    gr_1.show_bar()
    gr_1.set_data([1, 4, 3, 2])
    gr_1.set_show(fl_show=True)
    gr_1.show_bar()
