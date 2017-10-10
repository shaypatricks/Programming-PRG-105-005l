import random
global function_numbers

def main():
    # the program is going to be making a random numbers list
    function_numbers = []

    for x in range(20):
        function_numbers.append(random.randrange(1, 101, 1))

    x = user()
    function_numbers.append(x)
    print(function_numbers)


def user():
    user = int(input('Please enter a number between 1 and 100: '))
    print(user)
    return user
# the user number is added to the list last
print('----------------------------------------------------------------------------------------------------------------')




main()
