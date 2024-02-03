"""
ДОПОЛНИТЕЛЬНЫЕ МАТЕРИАЛЫ ПО ООП:

https://younglinux.info/oopython/inheritance

Практическая работа

Разработайте программу по следующему описанию.

В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем",
который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.

Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.

"""
from random import choice as rnd_choice
from tqdm import tqdm


class Unit:
    __UID = 0
    
    def __init__(self, team_id: int):
        __class__.__UID += 1
        self.uid = self.__UID
        self.team_id = team_id

    def __setattr__(self, key, value):
        if key == "team_id" and type(value) == int and value > -1:
            pass
        elif key == "team_id":
            raise TypeError('можно передавать только реальные (от 0 и больше) целочисленные значения')
        super().__setattr__(key, value)


class Hero(Unit):
    def __init__(self, team_id: int):
        super().__init__(team_id)
        self.level = 0

    def up_level(self):
        self.level += 1


class Soldier(Unit):
    pass


def prepare_container(container: dict = {}):
    if not len(container):
        return
    result_dict = {}
    for k in container:
        result_dict[k] = []
        result_dict[k].append(Hero(k))
    return result_dict


teams = {
    1: 'marshmallow trolls',
    2: 'mighty sparrows',
    3: 'flying nails',
    4: 'sober pigs',
    5: 'hustlers'
}


if __name__ == '__main__':
    sol_1 = Soldier(1)
    sol_1.team_id = 2
    hero_1 = Hero(1)
    hero_1.team_id = 2
    print(sol_1.__dict__)
    print(hero_1.__dict__)
    hero_1.up_level()
    print(hero_1.__dict__)

    units_container = prepare_container(teams)
    # print(units_container)

    iterations = 1000
    hero_uplevel_border = 11  # данное количество солдат увеличивает уровень героев на 1 единицу
    # print(33%hero_uplevel_border)
    unique_team_ids = set(teams)
    heroes_lst = [v[0] for (k,v) in units_container.items()]
    print(*heroes_lst, sep="\n")
    for i in tqdm(range(iterations)):
        tm = rnd_choice(list(unique_team_ids))
        units_container[tm].append(Soldier(tm))
        hero_tmp = units_container[tm][0]
        soldiers_num = len(units_container[tm]) - 1
        if not soldiers_num % hero_uplevel_border:
            hero_tmp.up_level()

    print(*["".join((str(k), " У команды ", teams[k], " солдат: ",
                     str(len(v) - 1), ", уровень героя: ", str(v[0].level)))
            for (k,v) in units_container.items()], sep="\n")
