class Dragon:
    CRITICAL_HP_PROPORTION = 0.3
    HP_MAX_VALUE = 10000
    DRAGONS_CREATED = dict()
    DONT_CREATE_NEW = False

    def __new__(cls, *args, **kwargs):
        # print(args)
        # print(kwargs)
        current_drgn_name = cls.__control_name(kwargs['name'])
        dragons_number_before = len(cls.DRAGONS_CREATED)
        # print(cls.DRAGONS_CREATED)
        if current_drgn_name not in cls.DRAGONS_CREATED:
            cls.DRAGONS_CREATED[current_drgn_name] = {}
        # print(cls.DRAGONS_CREATED)
        dragons_number_after = len(cls.DRAGONS_CREATED)
        if dragons_number_before == dragons_number_after:
            print(f'Дракон с именем <{current_drgn_name}> уже создан ранее!')
            # ПРЕДОТВРАЩАЕМ ПЕРЕЗАПИСЬ АТТРИБУТОВ ДАННОГО ЭКЗЕМПЛЯРА КЛАССА!!!
            cls.DONT_CREATE_NEW = True
            return cls.DRAGONS_CREATED[current_drgn_name]['obj']
        else:
            # в исходную!
            cls.DONT_CREATE_NEW = False
            print(f'Создаем Дракона с именем <{current_drgn_name}>')
            new_dragon = super().__new__(cls)
            cls.DRAGONS_CREATED[current_drgn_name]['obj'] = new_dragon
            return new_dragon

    def __init__(self,
                 age,
                 name,
                 color='Зеленый',
                 is_flying=True,
                 hit_points=900):
        if self.DONT_CREATE_NEW:
            pass
        else:
            self.age = age
            self.name = self.__control_name(name)
            self.__color = color
            self.__is_flying = is_flying
            self.__hit_points = hit_points
            self.__missiles_got = []
            self.__is_alive = True
            # порог ХитПойнтов, ниже которого дракон не сможет летать!
            self.__critical_hp = hit_points * self.CRITICAL_HP_PROPORTION
            print("НА ОДНОГО ДРАКОНА СТАЛО БОЛЬШЕ - ТРЕПЕЩИ ЧЕСТНОЙ НАРОД!")

    @classmethod
    def __control_natural_digit(cls, value, max_bound):
        if type(value) not in (int, float):
            False,0
        elif 0 <= value <= max_bound:
            return True, value
        elif 0 > value:
            return True, 0
        elif value > max_bound:
            return True, max_bound

    @classmethod
    def __control_name(cls, text):
        text = str(text).strip().lower()
        text = text.capitalize()
        return text

    def die(self):
        print(f"<{self.name}> покинул нас... после получения урона от <{self.__missiles_got[-1].name}>")
        self.__is_flying = False
        self.__is_alive = False

    def set_hit_points(self, hit_points):
        is_alive = self.__is_alive
        hp_sheck_result = self.__control_natural_digit(value=hit_points,
                                                  max_bound=self.HP_MAX_VALUE)
        if not hp_sheck_result[0]:
            print('Некорректное значение для характеристики Hit Points!')
        else:
            updated_hp = hp_sheck_result[1]
            self.__hit_points = updated_hp
            if updated_hp < self.__critical_hp:
                print(f"<{self.name}> получил критический урон!")
                self.__is_flying = False
            if updated_hp == 0:
                self.die()
            elif updated_hp and not is_alive:
                self.__is_alive = True
                print(f"<{self.name}> реинкарнировался!")

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
        self.__missiles_got.append(missile)
        missile.make_damage(victim_name=self.name)
        self.set_hit_points(self.__hit_points - missile.damage)

    def get_missiles(self):
        return self.__missiles_got

    def del_missile(self):
        missile = self.__missiles_got[-1]
        print(f"Из <{self.name}> был извлечен: <{missile.name}>")
        del self.__missiles_got[-1]

    missile = property(get_missiles, set_missile, del_missile)

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
    def __init__(self, name='Стрела', damage=0):
        self.name = name
        self.damage = damage

    def make_damage(self, victim_name):
        print(f'Снаряд <{self.name}> причинил <{self.damage}> урона <{victim_name}>')

    # финализатор снаряда, на который не ведут ссылки!
    def __del__(self):
        print(f'Удаление <{self.name}> - инициализировано.')
        del self
        print('Удаление снаряда успешно завершено!')
        try:
            print(f'<{self.name}>')
        except UnboundLocalError as e:
            print(f'Возникла ошибка при попытке вызвать имя экземпляра класса Missile <{e}>')


if __name__ == '__main__':
    Smaug = Dragon(age=579, name="Смауг", color='black')
    Smaug.color = 'Red'
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug.__dict__.items()], sep='\n')
    # лишаем дракона приватного свойства цвет!
    Smaug.del_color()
    # missl_1 = Missile(damage=35)

    print('\n 1-ый снаряд')
    Smaug.missile = Missile(damage=35)
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug.__dict__.items()]
          + [i.name for i in Smaug.missile], sep='\n')
    print('Удаляем снаряд, попавший в дракона последним:')
    del Smaug.missile
    Smaug.fly()
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug.__dict__.items()]
          + [i.name for i in Smaug.missile], sep='\n')

    print('\n 2-ой снаряд')
    missl_2 = Missile(name='Гарпун', damage=700)
    Smaug.missile = missl_2
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug.__dict__.items()]
          + [i.name for i in Smaug.missile], sep='\n')
    Smaug.fly()

    print('\n 3-ий снаряд')
    missl_3 = Missile(name='Ульта ЭлектроДрели', damage=55555)
    Smaug.missile = missl_3
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug.__dict__.items()]
          + [i.name for i in Smaug.missile], sep='\n')
    Smaug.fly()

    print()
    print('Снаряды, затрявшие в драконе (не были из него удалены):')
    print(*[(i, i.name) for i in Smaug.missile], sep='\n')
    print('Удаляем снаряд, попавший в дракона последним:')
    del Smaug.missile
    print('Снаряды, затрявшие в драконе (не были из него удалены):')
    print(*[(i, i.name) for i in Smaug.missile], sep='\n')

    print()
    print('Все переменные глобальной области видимости:')
    print(*[(k,v) for (k,v) in globals().items()], sep='\n')

    print()
    # print('пробуем присовить значению ХитПойнты некорректное значение!')
    # Smaug.set_hit_points(hit_points="777")
    print("Воскрешаем...")
    Smaug.set_hit_points(hit_points=20000)
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug.__dict__.items()], sep='\n')
    Smaug_2 = Dragon(age=333, name="Смауг ", color='purple')
    print(Smaug_2)
    print(*[(k,v) for (k,v) in Dragon.DRAGONS_CREATED.items()], sep='\n')
    print()
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug_2.__dict__.items()], sep='\n')
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Smaug.__dict__.items()], sep='\n')
    print(Smaug == Smaug_2)
    Golden_Dragon = Dragon(age=777, name=' драконИще ', color='khaki')
    print(*[f'Атрибут <{k}> = <{v}>' for (k, v) in Golden_Dragon.__dict__.items()], sep='\n')
    print(*[(k, v) for (k, v) in Dragon.DRAGONS_CREATED.items()], sep='\n')