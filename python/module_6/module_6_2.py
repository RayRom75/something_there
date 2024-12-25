#!/usr/bin/env python3

class Vehicle:
    __COLOR_VARIANTS = ["Белый", "Черный", "Красный", "Зеленый", "Синий", "Серый"]

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на", new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'синий', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Розовый')
vehicle1.set_color('ЧЕРНЫЙ')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
