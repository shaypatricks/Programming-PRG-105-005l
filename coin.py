import random
#simulate a coin flip
class Coin:
    def __init__(self):
        self.__side_up = 'Heads'


    def toss(self):
        if random.randint(0, 1) == 0:
            self.__side_up = 'Heads'
        else:
            self.__side_up = 'Tails'

    def get_side_up(self):
        return self.__side_up

def main():
    coin = Coin()
    heads = 0
    tails = 0
    for flip in range(0, 50):
        coin.toss()
        table = coin.get_side_up()
        if table == 'Heads':
            heads += 1
        else:
            tails += 1

    total = 50 - heads
    print('You got a total of', total, 'tails')


main()
