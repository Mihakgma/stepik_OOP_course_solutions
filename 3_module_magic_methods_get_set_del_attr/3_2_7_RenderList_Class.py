"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wp4CyhdXcbY

Подвиг 6. Предположим, вам необходимо создать программу по преобразованию списка строк, например:

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
в следующий фрагмент HTML-разметки (многострочной строки, кавычки выводить не нужно):

'''<ul>
<li>Пункт меню 1</li>
<li>Пункт меню 2</li>
<li>Пункт меню 3</li>
</ul>'''

Для этого необходимо объявить класс RenderList, объекты которого создаются командой:

render = RenderList(type_list)
где type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>).
Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.

Затем, предполагается использовать объект render следующим образом:

html = render(lst) # возвращается многострочная строка с соответствующей HTML-разметкой
Пример использования класса (эти строчки в программе писать не нужно):

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
P.S. На экран ничего выводить не нужно.
"""


class RenderList:
    tags_approved = {
        "ol": ["<ol>", "</ol>"],
        "ul": ["<ul>", "</ul>"]
    }
    default_tag = "ul"

    def __init__(self, type_list: str):
        """
        type_list - тип списка
        (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>).
        Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.
        """
        self.type_list = type_list if type_list in self.tags_approved else self.default_tag

    def get_tags(self, tags_type):
        tags_info = self.tags_approved
        if isinstance(tags_type, str):
            return [tags_info[self.default_tag], tags_info[tags_type]][tags_type in tags_info]
        return

    def __call__(self, *args, **kwargs):
        statement_rows = args[0]
        txt = '\n'.join([f'<li>{row}</li>' for row in statement_rows])
        tags = self.tags_approved[self.type_list]
        return f'{tags[0]}\n{txt}\n{tags[1]}'


# Далее - для проверки:
if __name__ == '__main__':
    tg_1 = RenderList("sdfnsdfsdf")
    print(tg_1.__dict__)
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
    render = RenderList("ol")
    html = render(lst)
    print(html)
