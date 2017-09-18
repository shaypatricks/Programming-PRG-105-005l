"""
 we are going to offer a monthly phone plan and calculate the cost
 Packages offered
 Package_A For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.

Package_B For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.

 Package_C For $69.99 per month unlimited minutes provided.

 Consumer will have $1250.00 in money to pay bills a month.
"""


bill = input("which Package did you purchase? ")

if bill == "A" or bill == "a" or bill == "B" or bill == "b" or bill == "C" or bill == "c":
    minutes = int(input("How many minutes did you use this month? "))

    if bill == "A" or bill == "a":
            if minutes > 450:
                price = 39.99 + (minutes - 450) * .45
                print("you owe $" + format(price, ",.2f"))
    elif bill == "B" or bill == "b":
            if minutes > 900:
                price = 59.99 + (minutes - 900) * .40
                print("You owe $" + format(price, ",.2f"))
    else:
        print("You have unlimited minutes you owe $69.99!")
else:
    print("Please Enter a Valid Package.")
