# import math to get full math library in python.
import math
# The idea is to get the user to choose any number to be raised by any number of power


def main():
    calc = int(input('What number do you require raised?:  '))
    power = int(input('How much do you want to raise the power of your number?: '))
    answer = power_calc(calc, power)
    print(answer)

# Make it go through if statements


def power_calc(power, calc):
    if power == 1:
        return calc

    if power != 1:
        return power**calc


main()
