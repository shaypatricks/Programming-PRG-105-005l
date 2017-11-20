"""
You will demonstrate Inheritance

1) In the first step you will create a parent class.
Create a parent class for Office Furniture. Set the class variables to be category
(desk, chair, filing cabinet would be examples), material, length, width, height, and price.
Include a method that returns a string about the object.

2. In the second step create a sub class for Desk that includes location_of_drawers
(left, right both are options) and number_drawers.
Override the parents __str__ method to include drawer location and count.

3. Implement each class in a separate file. Import these into your main program.
Your main program should implement and display an instance of each, the parent class and the child class.
"""

class Office(object): # The Creation of the marketing of furniture

         def __init__(self, product, quantity, price):

             self.__product = product
             self.__quantity = quantity
             self.__price = price

         def set_product(self, product):
             self.__product = product
         def set_quantity(self, quantity):
             self.__quantity = quantity
         def set_price(self, price):
             self.__price = price



         def get_product(self):
            return self.__product

         def get_quantity(self):
            return self.__quantity

         def get_price(self):
            return self.__price

         def get_item_price(self):
            return self.__price * self.__quantity

         def __str__(self):
            line_item = self.__product + "  qty-" + str(self.__quantity) + " each: ${:0,.2f}".format(self.__price) + "  total= ${:0,.2f}".format(self.get_item_price())
            return line_item


def main():
    desk_1 = Office('cedar desk', 12, 250)
    desk_3 = Office('oak desk',5, 450)
    desk_2 = Office('spruce desk', 2, 1500)
    chair_1 = Office('leather chair', 12, 50)
    chair_2 = Office('cloth chair', 12, 40)
    chair_3 = Office('plastic chair', 12, 25)
    print(desk_1)
    print(desk_2)
    print(desk_3)
    print(chair_1)
    print(chair_2)
    print(chair_3)
    print('\n')

# New Shipment and marketing Sales
    print(" our total storage")
    desk_1.set_price(150.00)
    chair_3.set_price(10.00)
    chair_2.set_price(35)
    print(desk_1)
    print(chair_3)
    print(chair_2)


    desk_2.get_price()
    print('\n')


    desk_2.set_quantity(15)

    print(desk_2)




main()
