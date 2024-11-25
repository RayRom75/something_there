#!/usr/bin/env python3

def count_calls():
    global calls
    calls = calls + 1

    return calls

def string_info(stroka):
    count_calls()

    return (len(stroka), stroka.upper(), stroka.lower())

def is_contains(stroka, stroks_list):
    count_calls()
    stroka = stroka.lower()

    for i in stroks_list:
        if (stroka == i.lower()):
            return True

    return False


calls = 0

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
