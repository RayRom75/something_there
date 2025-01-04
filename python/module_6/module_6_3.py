#!/usr/bin/env python3

import random

class Animal:

    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    live = True
    sound = None

    def __init__(self, speed):
        self.speed = speed
        pass

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        z = self._cords[2] + dz * self.speed
        if z < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[2] = z
        pass

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
        pass

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
            return
        print("Be careful, i'm attacking you 0_0" )
        pass

    def speak(self):
        print(self.sound)
        pass

class Bird(Animal):

    beak = True

    def lay_eggs(self):
        l = random.randint(1, 4)
        print(f"Here are(is) {l} eggs for you")
        pass


class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz) * (self.speed / 2))
        pass

class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
