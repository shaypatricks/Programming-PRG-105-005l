"""
Write a program that gets a string from the user containing a person's first, middle, and last names and then displays their
first, middle, and last initials.  (Creating a new variable and concatenating each letter plus a '.' is the easiest way to do this.)
For example, if the user enters John William Smith, the program should display J. W. S.
"""

# Start by getting user input for first, middle and last names
# Then split the names so its easier to retireve characters
# Then turn the split characters into a individual list
# Print name with intials


def main():
    first = input('Please enter your first name: ')
    middle = input('Please enter your middle name: ')
    last = input('Please enter you last name: ')
    name = first, middle, last
    first_split = first.split()
    middle_split = middle.split()
    last_split = last.split()
    first_list = first_split[0][0]
    middle_list = middle_split[0][0]
    last_list = last_split[0][0]
    print(name, "=", first_list.upper(), '.', middle_list.upper(), '.', last_list.upper())


main()
