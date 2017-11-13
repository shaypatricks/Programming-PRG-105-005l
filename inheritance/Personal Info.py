"""
Design a class that holds the following personal data: name, address, age, and phone number. Write appropriate accessor and mutator methods (get and set).
Also, write a program that creates three instances of the class. One instance should hold your information and the other two should hold information you make up.
Just add information, don't get it from the user.
For this assignment, a class diagram and an explanation of how the class diagram was created are provided for you.
In future assignments, you will have to plan your own project using class diagrams. This will replace pseudocode.
The video also explains what accessors and mutators are.
"""
# Make the class and its attributes


class Personal:
    def __init__(self, name, age, address, phone):
        self._personal_name = name
        self._personal_age = age
        self._personal_address = address
        self._personal_phone = phone
    # Time to set up the pieces

    def __set_personal_name(self, name):
        self._personal_name = name

    def __set_personal_age(self, age):
        self._personal_age = age

    def __set_personal_address(self, address):
        self._personal_address =address

    def __set_personal_phone(self, phone):
        self._personal_phone = phone
    # Get the personal Data

    def get__personal_name(self):
        return self._personal_name

    def get__personal_age(self):
        return self._personal_age

    def get__personal_address(self):
        return  self._personal_address

    def get__personal_phone(self):
        return self._personal_phone

    def get__personal_info(self):
        print(self._personal_name)
        print(self._personal_age)
        print(self._personal_address)
        print(self._personal_phone)

    # Now to make our data and print it


def main(self):
    name_1 = Personal(name='Steffen', address='4450 drake St', age='20', phone='123-456-7890')
    name_2 = Personal(name='Freddy', address='123, Elm St', age='75', phone='N/A')
    name_3 = Personal(name='Jason', address='Camp Crystal Lake', age='71', phone='N/A')

    name_1.get__personal_info()
    print('----------------------')
    name_2.get__personal_info()
    print('-----------------------')
    name_3.get__personal_info()


main('self')
