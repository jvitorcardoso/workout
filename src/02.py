# Summing numbers


def my_sum(*numbers: tuple) -> int:
    output = 0

    for number in numbers:
        output += number

    return f'{output}, even' if output % 2 == 0 else f'{output}, odd'


print(my_sum(1, 2, 3, 4))
