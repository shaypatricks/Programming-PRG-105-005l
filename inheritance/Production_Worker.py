"""
File 1:
Write an Employee class that keeps data attributes for the following pieces of information:
Employee name
Employee number
Next, Write a class named ProductionWorker that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes for the following information
Shift numbered (an integer, such as 1, 2, or 3)
Hourly pay rate
The workday is divided into two shifts: day and night.
The shift attribute will hold an integer value representing the shift that the employee works.
The day shift is shift 1 and the night shift is shift 2. Write the appropriate accessor and mutator methods
(get and set) for each class.
File 2:
Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts the user to
enter data for each of the object’s data attributes. Store the data in the object and then use the object’s accessor methods to retrieve it
and display it on the screen.
"""


class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.number = number

    def set_employee_name(self, name):
        self.__name = name

    def set_employee_number(self, number):
        self.__number = number

    def get_employee_name(self):
        return self.__name

    def get_employee_number(self):
        return self.number


class ProductionWorker(Employee):

    def __init__(self, name, number, shift_num, pay_rate):
        Employee.__init__(self, name, number)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_pay_rates(self):
        return self.__pay_rate


def main():

    print('enter following Details of the Employee')
    print('--------------------------------------------')
    employee_name = input('Enter Employee Name: ')
    number = int(input('Enter Employee Number: '))
    pay = int(input('Enter Pay Rate: '))
    x = 0

    while x == 0:
        shift = int(input('Enter Shift Number: '))
        if shift == 1:
            x = 1
            shift = 'Day'
        elif shift == 2:
            x = 2
            shift = 'Night'

    employee = ProductionWorker(employee_name, number, shift, pay)

    print('-------------------------------------------------------')
    print('Details of Employee:')
    print('-------------------------------------------------------')
    print('Name:', employee.get_employee_name())
    print('Employee Number:', employee.get_employee_number())
    print('Shift:', employee.get_shift_num())
    print('Pay Rate:', employee.get_pay_rates())


main()
