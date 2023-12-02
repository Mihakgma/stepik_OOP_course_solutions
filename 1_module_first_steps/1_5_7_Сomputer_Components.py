"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZTCdEB_6h1I

Подвиг 7. Объявите в программе следующие несколько классов:

CPU - класс для описания процессоров;
Memory - класс для описания памяти;
MotherBoard - класс для описания материнских плат.

Обеспечить возможность создания объектов каждого класса командами:

cpu = CPU(наименование, тактовая частота)
mem = Memory(наименование, размер памяти)
mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
Обратите внимание при создании объекта класса MotherBoard можно передавать
несколько объектов класса Memory, максимум N - по числу слотов памяти на материнской плате (N = 4).

Объекты классов должны иметь следующие локальные свойства:

для класса CPU: name - наименование; fr - тактовая частота;
для класса Memory: name - наименование; volume - объем памяти;
для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU;
total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти).

Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов
на материнской плате в виде следующего списка из четырех строк:

['Материнская плата: <наименование>',
'Центральный процессор: <наименование>, <тактовая частота>',
'Слотов памяти: <общее число слотов памяти>',
'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']

Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).

P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.
"""


class CPU:
    def __init__(self, name: str, fr: int):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name: str, volume: int):
        self.name = name
        self.volume = volume


class MotherBoard:
    total_mem_slots = 4

    def __init__(self, name: str, cpu: CPU, mem_slots: [Memory]):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        name = self.name
        cpu_name = self.cpu.name
        cpu_fr = self.cpu.fr
        total_mem_slots = self.total_mem_slots
        mem_slots = self.mem_slots
        memory_info = 'Память: ' + ('; '.join([f'{slot.name} - {slot.volume}'
                                               for slot in mem_slots]))
        config_info = [f'Материнская плата: {name}',
                       f'Центральный процессор: {cpu_name}, {cpu_fr}',
                       f'Слотов памяти: {total_mem_slots}',
                       memory_info]
        return config_info


if __name__ == '__main__':
    cpu_1 = CPU(name='Intel', fr=2000)
    mem_1 = Memory(name='Gigabyte', volume=4064)
    mem_2 = Memory(name='SVO', volume=1028)
    mb = MotherBoard(name='Intel',
                     cpu=cpu_1,
                     mem_slots=[mem_1, mem_2])
    current_config = mb.get_config()
    # Далее - для проверки!!!
    print(current_config)
