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


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

# __str__
print(h1)

print(h2)

# __len__
print(len(h1))

print(len(h2))
