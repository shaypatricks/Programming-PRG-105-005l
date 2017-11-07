"""
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
THe program should display a menu that lets the user look up a person's email address, add a new name and email address, ' \
change an existing email address, and delete an existing name and email address.
The program should pickle the dictionary and save it to a file when the user exits the program.
Each time the program starts, it should retrieve the dictionary from the file and unpickle it.

Make sure you use separate functions;, upload both the created text file and the program to GitHub.
Submit a link to the .py file and add a link to the text file in the comments.
"""

import pickle

# program will have keys to "Fast Travel" through program
LOOK_UP = 1
ADD_CONTACT = 2
CHANGE_CONTACT = 3
DELETE_CONTACT = 4
END_PROGRAM = 5


def contact():
    try:
        contact_folder = open('Contacts_file.dat', 'rb')
        contacts = pickle.load(contact_folder)
        print(contacts)
    except (FileNotFoundError, IOError):
        print('File not found please try again')
        contacts = {}
    user_input = 0

    while user_input != END_PROGRAM:
        user_input = main()

        if user_input == LOOK_UP:
            look_up(contacts)
        elif user_input == ADD_CONTACT:
            add_contact(contacts)
        elif user_input == CHANGE_CONTACT:
            change_contact(contacts)
        elif user_input == DELETE_CONTACT:
            delete_contact(contacts)
        elif user_input == END_PROGRAM:
            end_program(contacts)

def main():
    print('Contact Shortcuts')
    print('-------------------')
    print('Look_up: 1')
    print('Add_contact: 2')
    print('Change_Contact: 3')
    print('Delete_contact: 4')
    print('End_program: 5')

    user_input = int(input('Please Enter a command: '))

    while user_input < 1 or user_input > 5:
        user_input = int(input('Please Enter a Valid Command: '))
    return  user_input

def look_up(contacts):
        name = input('Enter contacts name: ')
        print(contacts.get(name, 'not found'))


def add_contact(contacts):
    name = input('Name: ')
    email = input('Email: ')
    if name not in contacts:
        contacts[name] = email
    else:
        print('This is already a contact.')


def change_contact(contacts):
    name = input('Name: ')
    if name in contacts:
        email = input('Email: ')
        contacts[name] = email
    else:
        print('This is not a saved contact.')


def delete_contact(contacts):
    name = input('Name: ')
    if name in contacts:
        del contacts[name]
    else:
        print('This name does not exist.')

def end_program(contacts):
    print('your contacts list is now updated and saved.')
    save_file = open('contacts_file.dat', 'wb')
    pickle.dump(contacts, save_file)
    save_file.close()


contact()
