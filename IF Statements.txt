# Variables And number of day each week
# The Idea is going to be an advertisement at a pizza joint each day of the week on what today sale is
# For The Question Type Anything that isn't sunday - Saturday ex. Halloween or Pizza
Today = input('Whats is it Today: ')
Sunday = 1
Monday = 2
Tuesday = 3
Wednesday = 4
Thursday = 5
Friday = 6
Saturday = 7

if Today == 'Sunday':
    print(" its Sunday today: Today's Special is a $14.99 2 Topping Pizza, Delivery only! ")
elif Today == 'Monday':
    print(" Its Monday today: Today's Special is Buy a Pizza Get a Free Appetizer of your choice!")
elif Today == 'Tuesday':
    print(" Its Tuesday today: Today's Special is buy one one-topping pizza get one for Half-off, carryout only!")
elif Today == 'Wednesday':
    print("Its Wednesday today: Today's Special is Get a family side pack meal with the purchase of 2 pizzas for free!")
elif Today == 'Thursday':
    print(" It's Thursday today: Today's Special is buy anyone 1 pizza get a free 2 liter soda! ")
elif Today == 'Friday':
    print(" Its Friday today: Today's Special Is buy any three topping pizza get the second one free, Carryout Only!")
elif Today == 'Saturday':
    print("Its Saturday today: Today's Special is get a Party Deal for Half off!")
else:
    print("Please Enter a Valid Date.")
