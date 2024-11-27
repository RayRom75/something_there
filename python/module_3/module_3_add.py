#!/usr/bin/env python3

def calculate_structure_sum(*args):
    sum_ = 0

    for argument in args:
        if isinstance(argument, int):
            sum_ += argument
        elif isinstance(argument, str):
            sum_ += len(argument)
        elif isinstance(argument, dict):
            for key, value in argument.items():
                sum_ += calculate_structure_sum(key, value)
        elif isinstance(argument, (list, set, tuple)):
                for i in argument:
                    sum_ += calculate_structure_sum(i)

    return sum_

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
