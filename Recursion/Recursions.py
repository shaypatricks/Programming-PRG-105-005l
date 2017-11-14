"""
Design a recursive function that accepts one integer argument, n, and prints the numbers 1 up through n. For example, if you call the function with n=5, you should see this:

1
2
3
4
5
"""


def main():
    user = input('Enter a string: ')
    message(int(input('Please enter a number to be recursed: ')), user)


def message(times, user):

    if times > 0:
        print(user)
        print(times, '.....')
        message(times - 1, user)
    else:
        print('NO!')


main()
