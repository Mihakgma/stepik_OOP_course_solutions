# пример создания защищенного атрибута извне. Так делать - НЕЛЬЗЯ КАТЕГОРИЧЕСКИ!!!
class OneMoreClass:
    def __init__(self) -> None:
        self.__a = 123123


if __name__ == '__main__':
    b = OneMoreClass()
    try:
        print(b.__a)
    except Exception as e:
        print(e)
    print(b.__dict__)
    hasattr(b, '__a')
    b.__a = 345345
    print(b.__a)
    print(b.__dict__)
    print(hasattr(b, '__a'), hasattr(b, '_OneMoreClass__a'))
    # print(b.__a == b._OneMoreClass__a)
