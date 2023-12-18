class Dragon:
    def __init__(self,  age, name, color='Зеленый', is_flying=True, missile=None, hit_points=900):
        self.age = age
        self.name = name
        self.__color = color
        self.is_flying = is_flying
        self.__missile = missile
        self.__hit_points = hit_points

    def __del__(self):
        print(f"<{self.name}> покинул нас... после получения урона от <{self.__missile.name}>")
        del self

    def set_hit_points(self, hit_points):
        self.__hit_points = hit_points
        if self.__hit_points <= 0:
            self.__del__()

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def del_color(self):
        del self.__color

    color = property()
    color = color.setter(set_color)
    color = color.getter(get_color)
    color = color.deleter(del_color)

    def set_missile(self, missile):
        self.__missile = missile
        self.set_hit_points(self.__hit_points - missile.damage)
        missile.make_damage(victim_name=self.name)

    def get_missile(self):
        return self.__missile

    def del_missile(self):
        missile = self.__missile
        print(f"Из <{self.name}> был извлечен снаряд: <{missile.name}>")
        del self.__missile

    missile = property(get_missile, set_missile, del_missile)


class Missile:
    def __init__(self, name='arrow', damage=0):
        self.name = name
        self.damage = damage

    def make_damage(self, victim_name):
        print(f'Снаряд <{self.name}> причинил <{self.damage}> урона <{victim_name}>')


if __name__ == '__main__':
    Smaug = Dragon(579, "Смауг", color='black')
    Smaug.color = 'Red'
    print(Smaug.__dict__)
    Smaug.del_color()
    missl_1 = Missile(damage=35)
    Smaug.missile = missl_1
    print(Smaug.__dict__)
    del Smaug.missile
    print(Smaug.__dict__)
    missl_2 = Missile(name='Гарпун', damage=9)
    Smaug.missile = missl_2
    print(Smaug.__dict__)
    print(isinstance(Smaug, Dragon))
