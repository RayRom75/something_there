#!/usr/bin/env python3

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
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
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
