import random
import time


def main():
    # get a random number
    number = random.randint(1, 10)
    # display random number
    time.sleep(1)
    print('the number is', number)
    main()


main()
