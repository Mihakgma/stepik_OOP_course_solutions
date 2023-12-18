class Dragon:
    CRITICAL_HP_PROPORTION = 0.3
    def __init__(self,
                 age,
                 name,
                 color='Зеленый',
                 is_flying=True,
                 missile_got=None,
                 hit_points=900):
        self.age = age
        self.name = name
        self.__color = color
        self.__is_flying = is_flying
        self.__missile_got = missile_got
        self.__hit_points = hit_points
        self.__is_alive = True
        self.__critical_hp = hit_points * self.CRITICAL_HP_PROPORTION

    def die(self):
        print(f"<{self.name}> покинул нас... после получения урона от <{self.__missile_got.name}>")
        self.__is_flying = False
        self.__is_alive = False

    def set_hit_points(self, hit_points):
        self.__hit_points = hit_points
        if hit_points < self.__critical_hp:
            print(f"<{self.name}> получил критический урон!")
            self.__is_flying = False
        if hit_points <= 0:
            self.die()

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
        self.__missile_got = missile
        missile.make_damage(victim_name=self.name)
        self.set_hit_points(self.__hit_points - missile.damage)

    def get_missile(self):
        return self.__missile_got

    def del_missile(self):
        missile = self.__missile_got
        print(f"Из <{self.name}> был извлечен снаряд: <{missile.name}>")
        del self.__missile_got

    missile = property(get_missile, set_missile, del_missile)

    def fly(self):
        is_alive = self.__is_alive
        is_flying = self.__is_flying
        if is_alive and is_flying:
            print(f"<{self.name}> взмахнул своими могучими крыльями и взмыл в небо.")
            return True
        elif not is_alive:
            print("Мертвые драконы не летают.")
            return False
        elif not is_flying:
            print(f"<{self.name}> не может взлететь.")
            return False


class Missile:
    def __init__(self, name='arrow', damage=0):
        self.name = name
        self.damage = damage

    def make_damage(self, victim_name):
        print(f'Снаряд <{self.name}> причинил <{self.damage}> урона <{victim_name}>')


if __name__ == '__main__':
    Smaug = Dragon(age=579, name="Смауг", color='black')
    Smaug.color = 'Red'
    print(*[(k, v) for (k, v) in Smaug.__dict__.items()], sep='\n')
    Smaug.del_color()
    missl_1 = Missile(damage=35)
    Smaug.missile = missl_1
    print(*[(k, v) for (k, v) in Smaug.__dict__.items()], sep='\n')
    del Smaug.missile
    Smaug.fly()
    print(*[(k, v) for (k, v) in Smaug.__dict__.items()], sep='\n')
    missl_2 = Missile(name='Гарпун', damage=700)
    Smaug.missile = missl_2
    print(*[(k, v) for (k, v) in Smaug.__dict__.items()], sep='\n')
    Smaug.fly()
    missl_3 = Missile(name='Ядро', damage=333)
    Smaug.missile = missl_3
    print(*[(k, v) for (k, v) in Smaug.__dict__.items()], sep='\n')
    Smaug.fly()
