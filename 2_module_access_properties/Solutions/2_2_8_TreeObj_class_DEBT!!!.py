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
        obj, prev = root, root
        i = -1
        while obj.indx > 0:
            print(obj.indx)
            prev = obj
            i += 1
            obj = [obj.right, obj.left][x[i]]
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
    print(root.__dict__)
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    print(root.__dict__)
    print(v_11.__dict__)
    print(v_12.__dict__)
    DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
    DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
    print(v_11.__dict__)
    print(v_12.__dict__)
    # print(root.__dict__)

    x = [1, 1, 0]
    res = DecisionTree.predict(root, x)  # будет программистом
    print(res)
    # "в классе DecisionTree должны быть методы add_obj и predict"
    print(hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree, 'predict'))

    # "в классе TreeObj должны быть объекты-свойства left и right"
    print(type(TreeObj.left) == property and type(TreeObj.right) == property)
    root = DecisionTree.add_obj(TreeObj(0))
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
    DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

    res_1 = DecisionTree.predict(root, [1, 1, 0])
    # 'программист', "неверный вывод решающего дерева"
    print(res_1)
    res_2 = DecisionTree.predict(root, [1, 0, 1])
    # 'нет', "неверный вывод решающего дерева"
    print(res_2)
    res_3 = DecisionTree.predict(root, [0, 1, 1])
    # 'посмотрим', "неверный вывод решающего дерева"
    print(res_3)
    print("Новые Тесты!!!")
    root = DecisionTree.add_obj(TreeObj(0))
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    v_111 = DecisionTree.add_obj(TreeObj(3), v_11)
    v_112 = DecisionTree.add_obj(TreeObj(4), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "1"), v_111)
    DecisionTree.add_obj(TreeObj(-1, "2"), v_111, False)
    DecisionTree.add_obj(TreeObj(-1, "5"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "6"), v_12, False)
    DecisionTree.add_obj(TreeObj(-1, "3"), v_112)
    DecisionTree.add_obj(TreeObj(-1, "4"), v_112, False)

    x = [1, 0, 1, 1, 0]
    res_7 = DecisionTree.predict(root, x)
    print(res_7)
