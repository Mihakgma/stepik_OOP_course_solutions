"""
Подвиг 9. Объявите класс с именем Figure и двумя атрибутами:

type_fig: 'ellipse'
color: 'red'
Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:

start_pt: (10, 5)
end_pt: (100, 20)
color: 'blue'
Удалите из экземпляра класса свойство color и выведите на экран список всех локальных свойств (без значений)
объекта fig1 в одну строчку через пробел в порядке, указанном в задании.
"""


class Figure:
    type = 'ellipse'
    color = 'red'


fig1 = Figure()
d = {
    'start_pt': (10, 5),
    'end_pt': (100, 20),
    'color': 'blue',
    'transparency': 70,
    'line_type': 'point',
}
[setattr(fig1, key, value) for key, value in d.items()]
del fig1.color
del fig1['line_type']

if __name__ == '__main__':
    print(*fig1.__dict__)