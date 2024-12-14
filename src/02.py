#!/usr/bin/env python3

"""Solution to chapter 1, exercise 2, beyond 1: my_sum with start"""


def my_sum(numbers: tuple, start=0) -> str:
    output = start

    for number in numbers:
        output += number

    return f'{output}, even' if output % 2 == 0 else f'{output}, odd'


print(my_sum((1, 2, 3, 4), 9,))
