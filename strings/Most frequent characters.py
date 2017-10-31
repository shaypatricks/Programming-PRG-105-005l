"""
Write a program that lets the user enter a string and displays the letter that appears most frequently in the string,
ignore spaces, punctuation, and Upper vs Lower case
Use appropriate variables, functions, and comments. Upload your pseudocode as a Word document, and hand in the
link to GitHub in the comments.
Hints:
Create a  list to hold letters based on the length of the user input
Convert all letters to the same case
Use a loop to check for each letter in the alphabet
Have a variable to hold the largest number of times a letter appears, and replace the value when a higher number is found
"""
import collections
# define mains function
def main():
    # Program will ask for user input and store it all in a dictionary
    user_input = input('Please enter a string: ')
    user_input = user_input.replace(" ", "")
    dictionary = {}
    # Run 2 for loops to count up the characters in a string
    for letters in user_input.lower():
        dictionary[letters] = 0
    for letters in user_input.lower():
         dictionary[letters] += 1
    dictionary = sorted(dictionary.items())

    # Get Results
    print('The most used letter in your string was', collections.Counter(user_input).most_common(1)[0])

# SUMMON MAIN


main()

