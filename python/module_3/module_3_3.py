#!/usr/bin/env python3

def print_params(a=1, b='строка', c=True):
    print(f'{a} {b} {c}')


values_list = [2, 'list', 2.1]
values_dict = {'a': 1, 'b': 'dict', 'c': False}
values_list_2 = [54.32, 'Строка']

print_params()

print_params(b=25)

print_params(c=[1, 2, 3])

print_params(*values_list)

print_params(**values_dict)

print_params(*values_list_2, 42)
