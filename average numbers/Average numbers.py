"""
Write a program that uses the numbers.txt file, which contains a series of integers. Your program will calculate the
average of all of the numbers stored in the file and display the average on the screen. Format to show a maximum of two
numbers to the right of the decimal point.
"""


def main():
# use a try and except statement to get the total and average of the numbers from the file
# the file will use a for loop and start at zero
    try:
        total = 0.0
        count = 0
        infile = open('numbers.txt', 'r')

        for line in infile:

            line = infile.readline()
            total += int(line)
            count+= 1

        print(total)

    except:
        print('Error')
    average = total/count
    print('the average is', format(average, '.2f'))
    print('Their was a total of 18 numbers.')

# close file
    infile.close()


main()
