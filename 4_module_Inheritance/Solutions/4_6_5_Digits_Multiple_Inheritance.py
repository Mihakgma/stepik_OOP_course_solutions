"""
Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам.
Выполним такой пример.



Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с
произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно.

https://stepik.org/lesson/702000/step/6?auth=registration&unit=702101
"""


from math import inf as infinity


class Digit:
    _types = (int, float)
    _min_max = ()

    def __init__(self, value):
        self.value = value

    def __setattr__(self, name, value):
        min_max = self._min_max
        if type(value) in self._types and not len(min_max):
            pass
        elif type(value) not in self._types or not min_max[0] <= value <= min_max[1]:
            raise TypeError('значение не соответствует типу объекта')
        self.__dict__.update({name: value})


class Integer(Digit):
    _types = (int,)

    def __init__(self, value):
        super().__init__(value)


class Float(Digit):
    _types = (float,)

    def __init__(self, value):
        super().__init__(value)


class Positive(Digit):
    _min_max = (0, infinity)

    def __init__(self, value):
        super().__init__(value)


class Negative(Digit):
    _min_max = (-infinity, 0)

    def __init__(self, value):
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


if __name__ == '__main__':
    digits = [PrimeNumber(i) for i in range(1, 4)]
    float_digits = [FloatPositive(float(i)) for i in range(1, 6)]
    digits.extend(float_digits)
    lst_positive = filter(lambda x: isinstance(x, Positive), digits)
    lst_float = filter(lambda x: isinstance(x, Float), digits)

    # Далее - для проверки!
    print(*[obj.value for obj in lst_positive], sep="\n")
    print("-----||||-----")
    print(*[obj.value for obj in lst_float], sep="\n")
    print("-----||||-----")
    print(*[obj.value for obj in digits], sep="\n")
    d_1 = Digit(1)
    print(d_1.__dict__)

    i_1 = Integer(123)
    print(i_1.__dict__)

    f_1 = Float(3.33)
    print(f_1.__dict__)

    p_1 = Positive(5.55)
    print(p_1.__dict__)

    p_2 = Positive(5)
    print(p_2.__dict__)

    # p_3 = Positive(-5)  # TypeError: значение не соответствует типу объекта
    fp_1 = FloatPositive(1.0)
    print(fp_1.__dict__)
