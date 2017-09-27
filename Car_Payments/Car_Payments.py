def main():
    car_payment = get_info()
    yearly(car_payment)


def get_info():
    car_loan = float(input('Please enter your total car loan payment: $ '))
    insurance = float(input('Please enter your insurance payment:  $ '))
    gas = float(input('please enter how much you spent in gas: $ '))
    maintenance = float(input('please enter how much you put into maintenance on your car: $ '))
    total = (car_loan + insurance + gas + maintenance)
    print('Your total monthly expenses are: $ ' + format(total, ',.2f'))
    return total


def yearly(monthly):
    yearly_costs = monthly * 12
    print('Your yearly cost is: $' + format(yearly_costs, ',.2f'))


main()
