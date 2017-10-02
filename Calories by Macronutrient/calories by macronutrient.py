"""
This program is going to be an automated computer gym calories count the program will do the following
 1: ask for your name
 2: will give you a greeting like a computer would
 3: computer is going to ask how many meals you ate then add the total of all your meals
 4: computer is then going to tell you how healthy you are in total calories
 5: program will then ask if you want to reset
 6: I did this to add more creativity and challenge to my self i know it isn't in the instruction.
 """

global carbs_totals
global fat_totals
global protein_totals



def main():
    name = input('what is your name member: ')
    print("Thank you " + name + " for using our Gym certified calories calculator we made this program to help show how many calories you've had and to show how your diet is.")


def calc():
    meal_intake = int(input("How many meals have you'd eaten for today?: "))
    global carbohydrates
    global fat
    global protein

    carbs_totals = 0
    fat_totals = 0
    protein_totals = 0

    if meal_intake > 3:
        print("You are snacking to much, this machine is going to calculate your three main meals.")
        for meals in range(3):
            print('meals')
            print('---------------------------------')
            carbohydrates = int(input('How many grams of carbohydrates have you eaten today: '))
            carbs_totals += carbohydrates
            fat = int(input('How many grams of fat did you eat: '))
            fat_totals += fat
            protein = int(input('How many grams of protein did you eat: '))
            protein_totals += protein
            print("The current totals are: Carbs: " + str(carbs_totals) + "; Fat: " + str(fat_totals) + ";protein: " + str(protein_totals))

    elif meal_intake <= 3:
        for meals in range(meal_intake):
            print('meals')
            print('--------------------------------')
            carbohydrates = int(input('How many grams of carbohydrates have you eaten today: '))
            carbs_totals += carbohydrates
            fat = int(input('How many grams of fat did you eat: '))
            fat_totals += fat
            protein = int(input('How many grams of protein did you eat: '))
            protein_totals += protein
            print("The current totals are: Carbs: " + str(carbs_totals) + "; Fat: " + str(fat_totals) + ";protein: " + str(protein_totals))
    # Now our computer is going to calculate show how many calories you consumed today individually
    print("---------------------------------")
    print("Separate Calories totals")
    print("---------------------------------")
    carbs_cal = carbs_totals*4
    print("you've  had ",  carbs_cal, " calories in  carbohydrates!")
    fat_cal = fat_totals*9
    print("you've had ", fat_cal, "calories in fat!")
    protein_cal = protein_totals*4
    print("you've had ", protein_cal, "calories in protein")
    print('---------------------------------------------')
    print('total daily calorie intake')
    print('----------------------------------------------')
    total_cal = carbs_cal + fat_cal + protein_cal
    print("You have eaten a total of", total_cal, "calories today.")


main()

print('-----------------------------------------------------------')

calc()



