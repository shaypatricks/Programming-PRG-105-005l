'''
def main():
    my_name = get_name()
    print('Hello', my_name, 'how may we help today')

def get_name():
    name = input('please enter your name: ')
    return name

main()

keep_going = 'y'

while keep_going == 'y' or keep_going == 'Y':
    income = float(input('Please enter your income to the month: $ '))
    bills = int(input('How many bills have you received: $ '))
for bills in range(bills):
    total = 0.00
    spending_money = income - bills

'''

# get cost from user, pass to calc_cost


def main():
    structure_value = float(input('how much would it cost to replace your home: $ '))
    calc_cost(structure_value)

# calculate the cost of the insurance using the variable


def calc_cost(value):
    insurance = value * .8
    print('you should get about $', format(insurance, ',.2f'), 'for your home.')


main()

