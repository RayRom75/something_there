#!/usr/bin/env python3

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        pass

    def __str__(self):
        return f"{self.nickname}"
        pass

    def __int__(self):
        return int(self.age)
        pass
