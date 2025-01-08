#!/usr/bin/env python3

from math import pi, sqrt

class Figure:

    sides_count = 0
    __sides = []
    __color = [0, 0, 0]
    filled = False

    def __init__(self, color, sides_count):
        if isinstance(color, tuple):
            self.set_color(color[0], color[1], color[2])
        self.sides_count = sides_count
        pass

    def get_color(self):
        return self.__color
        pass

    def __is_valid_color(self, r, g, b):
        return (r >= 0 and r < 256) and (g >= 0 and g < 256) and (b >= 0 and b < 256)
        pass

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        pass

    def get_sides(self):
        return self.__sides
        pass

    def __is_valid_sides(self, sides):
        return sides > 0 and sides == self.sides_count
        pass

    def set_sides(self, *new_sides):
        if (self.__is_valid_sides(len(new_sides))):
            self.__sides = []
            for i in range(len(new_sides)):
                self.__sides.append(new_sides[i])
        else:
            side = 1
            if len(new_sides) == 1:
                side = new_sides[0]
            elif self.__sides != []:
                return

            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(side)
        pass

class Circle(Figure):

    def __init__(self, color, *side):
        super().__init__(color, 1)
        self.set_sides(*side)
        self.__radius = self.get_sides()[0] / pi
        pass

    def get_square(self):
        return  pi * self.__radius ** 2
        pass

    def __len__(self):
        return self.get_sides()[0]
        pass

class Triangle(Figure):

    def __init__(self, color, *sides):
        super().__init__(color, 3)
        self.set_sides(*sides)
        pass

    def get_square(self):
        [a, b, c] = self.get_sides()
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))
        pass

class Cube(Figure):

    def __init__(self, color, side):
        super().__init__(color, 12)
        self.set_sides(side)
        pass

    def get_volume(self):
        return self.get_sides()[0] ** 3
        pass

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
