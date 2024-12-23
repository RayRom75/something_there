#!/usr/bin/env python3

class Plant:
    edible = False
    name = None

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.name = args[0]
        return obj

class Animal:
    alive = True
    fed = False
    name = None

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.name = args[0]
        return obj

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    def __str__(self):
        return self.name

class Fruit(Plant):
    edible = True

    def __str__(self):
        return self.name

class Mammal(Animal):
    def __str__(self):
        return self.name

class Predator(Animal):
   def __str__(self):
       return self.name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
