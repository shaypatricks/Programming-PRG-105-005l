"""
Write a program that reads the contents of the two files into two separate lists.
The user should be able to enter a boy's name, a girl's name, or both* and the application will display messages
indicating whether the names were among the most popular.
* Entering a name should cause the program to check both lists.
"""

def main():
    # start with opening both files

    pop_girls = open('GirlNames.txt', 'r')
    pop_boys = open('BoyNames.txt', 'r')
    user_check = input('Please enter a name: ')
    name_1 = pop_girls.readline()
    name_2 = pop_boys.readline()
    pop_girls.close()
    pop_boys.close()
    name_g = name_1.rstrip('\n')
    name_b = name_2.rstrip('\n')

    # now to run a user input
    for line in name_g:
        line = name_g
        if user_check == name_g:
            print('This is a popular girls name')
        else:
            print("This is not a popular girls name")
        break
    for line1 in name_b:
        line1 = name_b
        if user_check == name_b:
            print('This is a popular boys name')
        else:
            print('this is not a popular boys name')
        break

main()
