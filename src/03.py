#!/usr/bin/env python3

"""My solution to exercise 3, chapter 1: Run timing"""

def run_timing() -> str:
    total, count = 0, 0

    while kilometers := input("Enter 10 km run time: "):
        if kilometers.isdigit():
            total += int(kilometers)
            count += 1
        elif kilometers == '':
            break
            
    return f'Average of {total / count}, over {count} runs'


print(run_timing())
