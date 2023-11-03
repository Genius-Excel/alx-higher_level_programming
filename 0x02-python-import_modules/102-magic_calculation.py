#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        sum_result = add(a, b)
        for num in range(4, 6):
            sum_result = add(sum_result, num)

        return sum_result

    else:
        return sub(a, b)
