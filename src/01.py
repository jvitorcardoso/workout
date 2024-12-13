# Write a function (guessing_name) that takes no arguments.
# When run, the function chooses a random integer between 0 and 100 (inclusive).

from random import randint


def guessing_name():
    return randint(0, 100)


real_number = guessing_name()
count = 1

while guess := input('Enter a number between 0 and 100: '):
    if guess.isdigit() and int(guess) >= 0 and int(guess) <= 100:
        guess = int(guess)
        if guess == real_number:
            print('INCREDIBLE! You guess the number at the FIRST attempt!')
        else:
            while guess != real_number:
                if guess < real_number:
                    count += 1
                    guess = input("Too low! I'll give you a %r° chance: " % count)
                    if guess.isdigit() and int(guess) >= 0 and int(guess) <= 100:
                        guess = int(guess)
                    else:
                        while not guess.isdigit() or not (int(guess) >= 0 and int(guess) <= 100):
                            guess = input("Invalid input. Enter a number between 0 and 100: ")
                elif guess > real_number:
                    count += 1
                    guess = input("Too high! I'll give you a %r° chance: " % count)
                    if guess.isdigit() and int(guess) >= 0 and int(guess) <= 100:
                        guess = int(guess)
                    else:
                        while not guess.isdigit() or not (int(guess) >= 0 and int(guess) <= 100):
                            guess = input("Invalid input. Enter a number between 0 and 100: ")
            else:
                print('Awesome! You guess the number at the %r° attempt!' % count)
            break
    else:
        while not guess.isdigit() or not (int(guess) >= 0 and int(guess) <= 100):
            guess = input("Invalid input. Enter a number between 0 and 100: ")
