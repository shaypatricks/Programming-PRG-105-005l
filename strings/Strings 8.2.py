"""
Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX. The
application should display the telephone number with any alphabetic characters that appeared in the original translated
to their numeric equivalent. For example, if the user enters 555-GET-FOOD the application should display 555-438-
3663
"""


def main():
    # the number index
    """
    a, b, c = 2

    d, e, f = 3

    g, h, i = 4

    j, k, l = 5

    m, n, o = 6

    p, q, r, s = 7

    t, u, v, = 8

    w, x, y, z = 9
    """
# the user is to enter a phone number with words like ex 1-800-jon-lent and get it translated to an actual number
    phone_number = input('Enter a phone number in the format of XXX-XXX-XXXX for translation: ')
    phone_number = phone_number.lower()
    print(phone_number)
    trans_numb = ''
# the for loop which will go through the user input and translate it
    for char in phone_number:
        if char.isdigit():
            trans_numb += char
        elif char.isalpha():
            if char == 'a' or char == 'b' or char == 'c':
                trans_numb += '2'
            elif char == 'd' or char == 'e' or char == 'f':
                trans_numb += '3'
            elif char == 'g' or char == 'h' or char == 'i':
                trans_numb += '4'
            elif char == 'j' or char == 'k' or char == 'l':
                trans_numb += '5'
            elif char == 'm' or char == 'n' or char == 'o':
                trans_numb += '6'
            elif char == 'p' or char == 'q' or char == 'r' or char == 's':
                trans_numb += '7'
            elif char == 't' or char == 'u' or char == 'v':
                trans_numb += '8'
            elif char == 'w' or char == 'x' or char == 'y' or char =='z':
                trans_numb += '9'
        else:
            trans_numb += char
# display translated number
    print(trans_numb)


main()
