"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/5Y9qT5grunw

Большой подвиг 8. Требуется реализовать программу по работе с решающими деревьями:



Здесь в каждом узле дерева делается проверка (задается вопрос). Если проверка проходит,
то осуществляется переход к следующему объекту по левой стрелке (с единицей),
а иначе - по правой стрелке (с нулем). И так до тех пор,
пока не дойдем до одного из листа дерева (вершины без потомков).

В качестве входных данных используется вектор (список) с бинарными значениями: 1 - да, 0 - нет.
Каждый элемент этого списка соответствует своему вопросу (своей вершине дерева), например:



Далее, этот вектор применяется к решающему дереву, следующим образом.
Корневая вершина "Любит Python" с ней связан первый элемент вектора x и содержит значение 1, следовательно,
мы переходим по левой ветви. Попадаем в вершину "Понимает ООП". С ней связан второй элемент вектора x со значением 0,
следовательно, мы переходим по правой ветви и попадаем в вершину "будет кодером".
Так как эта вершина конечная (листовая), то получаем результат в виде строки "будет кодером".
По аналогии выполняется обработка вектора x с другими наборами значений 0 и 1.

Для реализации решающих деревьев в программе следует объявить два класса:

TreeObj - для описания вершин и листьев решающего дерева;
DecisionTree - для работы с решающим деревом в целом.

В классе DecisionTree должны быть реализованы (по крайне мере) два метода уровня класса (@classmethod):

def predict(cls, root, x) - для построения прогноза (прохода по решающему дереву)
для вектора x из корневого узла дерева root.
def add_obj(cls, obj, node=None, left=True) - для добавления вершин в решающее дерево
(метод должен возвращать добавленную вершину - объект класса TreeObj);

В методе add_obj параметры имеют, следующие значения:

obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
node - ссылка на объект дерева, к которому присоединяется вершина obj;
left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj
(True - к левой ветви; False - к правой).

В классе TreeObj следует объявить инициализатор:

def __init__(self, indx, value=None): ...

где indx - проверяемый в вершине дерева индекс вектора x; value - значение, хранящееся в вершине
(принимает значение None для вершин, у которых есть потомки - промежуточных вершин).

При этом, в каждом создаваемом объекте класса TreeObj должны автоматически появляться следующие локальные атрибуты:

indx - проверяемый индекс (целое число);
value - значение с данными (строка);
__left - ссылка на следующий объект дерева по левой ветви (изначально None);
__right - ссылка на следующий объект дерева по правой ветви (изначально None).

Для работы с локальными приватными атрибутами __left и __right необходимо объявить
объекты-свойства с именами left и right.

Эти классы в дальнейшем предполагается использовать следующим образом (эти строчки в программе не писать):

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class TreeObj:
    def __init__(self, indx=0, value: str=None):
        """
        Метод-иницализатор
        :param indx: уровень в иерархии дерева от корня (0 - корень, 1- след уровен, и т.д.)
        :param value: значение с данными (строка)
        """
        self.indx = indx
        self.value = value
        self.__left: TreeObj = None
        self.__right: TreeObj = None

    def get_left(self):
        return self.__left

    def set_left(self, lft):
        self.__left = lft

    left = property(get_left, set_left)

    def get_right(self):
        return self.__right

    def set_right(self, rght):
        self.__right = rght

    right = property(get_right, set_right)


class DecisionTree:
    @classmethod
    def predict(cls, root: TreeObj, x: list):
        """
        для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root.
        :param root: объект класса TreeObj, от которого мы "шагаем" (ведем обход) по дереву
        :param x: лист с путем по дереву со значениями 1 или 0
        :return: value - значение с данными (строка) из целевого объекта
        """
        if not len(x):
            return
        next = [root.right, root.left][x[0]]
        if len(x) == 1:
            pass
        else:
            for i in x[1:]:
                print(i)
                prev = next
                next = [next.right, next.left][i]
        try:
            return next.value
        except AttributeError:
            return prev.value

    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj=None, left: bool=True):
        """
        Обрабатывает текущий обьект obj, т.е. переприсваиваем ему значения атрибутов
        :param obj: сам объект
        :param node: объект дерева, из которого "растет" текущий объект
        :param left: ответ верный (1)
        :return: текущий обьект obj
        """
        if node is None:
            return obj
        if left:
            node.left = obj
        else:
            node.right = obj
        return obj


# Далее - для проверки!
if __name__ == '__main__':
    root = DecisionTree.add_obj(TreeObj(0))
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
    DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
    print(root.__dict__)

    x = [0, 1, 0]
    res = DecisionTree.predict(root, x)  # будет программистом
    print(res)
