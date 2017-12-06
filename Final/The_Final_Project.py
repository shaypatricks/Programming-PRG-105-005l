# import all assist
import random
import time

# Intro

print("Welcome to Dragon Star Tavern")
time.sleep(1)
print("Come in and relax by the fire from the stress of adventuring my friend")
time.sleep(1)

# Define the player class


class Player:
    def __init__(self, name, gold, drinks):
        self.__name = name
        self.__gold = gold
        self.__drinks = drinks

    def set_name(self, name):
        self.__name = name

    def set_gold(self, gold):
        self.__gold = gold

    def set_drinks(self, drinks):
        self.__drinks = drinks

    def get_name(self):
        return self.__name

    def get_gold(self):
        return self.__gold

    def get_drinks(self):
        return self.__drinks

# Main will receive players name
# around program to different functions and keep returned data


def main():

    player = Player('', '', '',)

    player.set_name(input('Whats your name Stranger?: '))
    player.set_gold(100)
    player.set_drinks(0)
    print('Welcome', player.get_name(), 'Enjoy the luxuries and hospitality of my Inn.')
    print('Go play some games,', player.get_name(), 'or come grab a drink.')
    print('You Currently have: ', player.get_gold(), 'gold')
    print('You Have currently drank:', player.get_drinks(), 'drinks.')
    print('------------------------------------------------------------')
    romes(player)

# romes is the key to track progress through the program and keep moving through


def romes(player):
    print('you currently have', player.get_gold(), 'gold')
    print('you have had', player.get_drinks(), 'drinks')

    print('key: \n', 'g = game \n', 'e = fortune teller \n', 'r = drink at bar \n', 'l = leave the bar')
    print('----------------------------------------------------------------------------------------------')
    roam = input('Where do you wish to go?: ')

    while roam in roam:
        if roam == 'g':
            liar_dice(player)
        elif roam == 'e':
            fortune_tellers(player)
        elif roam == 'r':
            drink(player)
        elif roam == 'l':
            leave(player)
        else:
            print('enter a valid response:')
        break
# Game 1 Liar dice


def liar_dice(player):
    print('you have:', player.get_gold(), 'gold')
    print('Do you know how to play', player.get_name() + '?')
    rules = input()
    no = 'You have 4 dice and your goal is to make your dice add up to 18 no more or your out, closest to 18 wins the pot'
    yes = 'ok'
    # the game will either display the rules or it will just move on!
    if rules == 'no':
        print(no)
    elif rules == 'yes':
        print(yes)
    elif rules == 'leave':
        print(player.get_gold())

    time.sleep(1)
    print('good luck')
    pro = 0
    opponent = 0

    choice = 'y'
    # while loop to allow the game to repeat in rounds
    while choice == 'y' or choice == 'Y':
        # for loop to do the dice game
        for dice in range(1):
            print(player.get_name())
            print('-----------------')
            dice_1 = random.randint(1, 6)
            print(dice_1)
            dice_2 = random.randint(1, 6)
            print(dice_2)
            dice_3 = random.randint(1, 6)
            print(dice_3)
            dice_4 = random.randint(1, 6)
            print(dice_4)
            pro_tot = pro + dice_1 + dice_2 + dice_3 + dice_4
            time.sleep(1)
            print(player.get_name(), 'scored', pro_tot)
            print('Opponent')
            print('--------------------------')
            dice_5 = random.randint(1, 6)
            print(dice_5)
            dice_6 = random.randint(1, 6)
            print(dice_6)
            dice_7 = random.randint(1, 6)
            print(dice_7)
            dice_8 = random.randint(1, 6)
            print(dice_8)
            pro_opp = opponent + dice_5 + dice_6 + dice_7 + dice_8
            print('Opponent scored', pro_opp)
            print('---------------')
            if pro_tot > 18:
                print("YOU BUSTED")
                loss = player.get_gold() - 10
                player.set_gold(loss)
            if pro_tot < pro_opp and pro_opp < 18:
                print('You Lost')
                print(' You lost 10 gold')
                loss = player.get_gold() - 10
                player.set_gold(loss)
            if pro_tot > pro_opp and pro_opp < 18:
                print('You Won')
                print('You received 10 gold')
                gain = player.get_gold() + 10
                player.set_gold(gain)
            if pro_opp > 18:
                print('Opponent Busted ')
                gain = player.get_gold() + 10
                player.set_gold(gain)
            if pro_tot == pro_opp:
                print('Draw \nno gold will be handed out')

        choice = input('Do you want to play another round?' "(press 'y' for yes) ")
    print('You walk away from the dice table.')
    romes(player)


def fortune_tellers(player):
    fortune_teller = fortune_file()
    x = random.randint(1, 100)

    input('Aah a wearied traveller visits me ask and i will answer!: ')

    answer = x % 15

    print(fortune_teller[answer])
    print('the fortune teller shoos you away.')
    print('------------------------------------')
    romes(player)


def fortune_file():

    meb = []

    infile = open('magic_eight_ball', 'r')

    temp = infile.readline()
    temp = temp.rstrip('\n')

    while temp != "":
        meb.append(temp)
        temp = infile.readline()
        temp = temp.rstrip('\n')

    infile.close()

    return meb


def drink(player):
    choice = 'y'
    print('You sit at the bar and order a drink')
    while choice == 'y' or choice == 'Y':
        drinker = player.get_drinks() + 1
        player.set_drinks(drinker)
        print(drinker, 'drink consumed')
        print("drinks: " + str(drinker))

        choice = input('Do you want another drink? ')
    print('you walk away from the bar')
    romes(player)


def leave(player):
    print('Have a nice night', player.get_name())
    print('You left with', player.get_gold(), 'gold')
    print('you had', player.get_drinks(), 'drinks')
    exit()


main()
