#!/usr/bin/env python3

def get_multiplied_digits(number):
    if number == 0:
            return 1

    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 0:
        last = str_number[1:]

        if len(last) > 0:
            return first * get_multiplied_digits(int(last))

        return first


result = get_multiplied_digits(40203)

print(result)

result2 = get_multiplied_digits(402030)

print(result2)
