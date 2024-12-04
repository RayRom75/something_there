#!/usr/bin/env python3

def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()

# inner_function()
#
# Я в области видимости функции test_function
# Traceback (most recent call last):
#   File "/home/rayrom/work/python/something_there/python/module_4/namespace.py", line 21, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
