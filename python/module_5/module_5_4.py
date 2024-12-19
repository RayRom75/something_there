#!/usr/bin/env python3

class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
        pass

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        pass

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории.')
        pass

    def go_to(self, new_floor):
        if new_floor < 1 or self.number_of_floors < new_floor:
            print('Такого этажа не существует.')
            return

        for i in range(new_floor):
            print(i + 1)
        pass

    def __len__(self):
        return self.number_of_floors
        pass

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
        pass

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Неверный тип данных')
        pass

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Неверный тип данных')
        pass

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Неверный тип данных')
        pass

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Неверный тип данных')
        pass

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Неверный тип данных')
        pass

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Неверный тип данных')
        pass

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        else:
            print(f'{value} не является целым числом')

        return self
        pass

    def __radd__(self, value):
        return self.__add__(value)
        pass

    def __iadd__(self, value):
        return self.__add__(value)
        pass

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
