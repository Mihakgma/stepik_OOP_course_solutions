"""
https://stepik.org/lesson/701998/step/4?unit=702099
"""


class Auto:
    __MIN_WEIGHT = 100
    __MAX_WEIGHT = 2500

    def __new__(cls, *args, **kwargs):
        if cls == Auto:
            raise TypeError("невозможно создать объект класса Auto")
        else:
            return super().__new__(cls)

    def __init__(self, model):
        self.__verify_model(model)
        self.__model = model
        self._min_weight = self.__MIN_WEIGHT
        self._max_weight = self.__MAX_WEIGHT

    def __verify_model(self, model):
        brand = self.__get_brand()
        # print(car_brand)
        if type(model) != str or brand not in model:
            raise TypeError(f'модель должна представляться строкой и содержать ключевое слово (марку авто): <{brand}>')

    def _verify_weight(self, weight):
        if not self._min_weight <= weight <= self._max_weight:
            brand = self.__get_brand()
            raise TypeError(
                f'вес автомобиля марки: <{brand}> должен быть в пределах [{self._min_weight}; {self._max_weight}] кг.')

    def __get_brand(self):
        return self.__class__.__name__


class BMW(Auto):
    def __init__(self, model, weight):
        super().__init__(model)
        self._verify_weight(weight)
        self.__weight = weight


class Kiira(Auto):
    """
    https://ru.wikipedia.org/wiki/Kiira_Motors_Corporation
    """

    def __init__(self, model, weight):
        super().__init__(model)
        self._verify_weight(weight)
        self.__weight = weight


if __name__ == '__main__':
    # auto_test = Auto("Kia")  # TypeError
    # print(auto_test)
    bmw_x5 = BMW('BMW X5', 2312.5)
    print(bmw_x5._BMW__weight)
    print(bmw_x5._Auto__model)
    print(bmw_x5.__dict__)
    # bmw_XZ = BMW('XZ', 1512.5)  # TypeError
    # print(bmw_XZ)
    kiira_evs = Kiira('Kiira EVS', 1250)
    print(kiira_evs._Kiira__weight)
    print(kiira_evs._Auto__model)
    print(kiira_evs.__dict__)
    