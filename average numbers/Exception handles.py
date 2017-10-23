"""
Copy your file from the previous exercise (Average numbers) and modify it so that it handles the following exceptions:
It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to
a number.
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

    # make exception errors
    except ValueError:
        print('Value Error, please try again.')

    except IOError:
        print('IoError, please try again.')

    except:
        print('Error')
    average = total/count
    print('the average is', format(average, '.2f'))
    print('Their was a total of 18 numbers.')





main()
