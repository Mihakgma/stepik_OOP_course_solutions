class property:
    def __set_name__(self, owner, name):
        setattr(self, "name", "_" + owner.__qualname__ + "__" + name)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Circle:
    x = property()
    y = property()
    radius = property()

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key, value):
        if key in ("x", "y", "radius") \
                and type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == "radius" \
                and value <= 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
