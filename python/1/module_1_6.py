#!/usr/bin/env python3

my_dict = {"Екатерина": 47, "Виталий": 49, "Александр": 25}
print("Dict:", my_dict)
print("Existing value:", my_dict["Александр"])
print("Not existing value:", my_dict.get("Сергей"))
print("Deleted value:", my_dict.pop("Александр"))
print("Modified dictionary:", my_dict)

print()
my_set = {1, 1, 2, 5, 2, True, True, (1, 2, 3, 4), "Вася", 3.14}
print("Set: ", my_set)
my_set.add("Added string")
my_set.add(2.27)
my_set.discard(3.14)
print("Modified set:", my_set)
