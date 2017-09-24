# how many pennies did i earn after _________ days
days = int(input("How many days have you worked: "))
print('---------------------------------------------')
pay = .01
total = 0
for day in range(0, days):
    print(str(day+1) + " $" + format(pay, ",.2f"))
    total += pay
    pay = pay * 2
print('------------------------------------------')
print("Total earned is $" + format (pay, ",.2f"))
