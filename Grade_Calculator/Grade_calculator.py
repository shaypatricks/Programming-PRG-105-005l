'''
def main():

    # Main is usually used to organize the data in the rest of the program
    average = one(5, 10, 15, 20, 25)
    function_two(average)

def one(one, two, three, four, five):
    # This function returns the average at five numbers
    ave = (one + two + three + four + five) /5
    return ave

def function_two(average_in):
    print ('The average of your five numbers is: ', average_in)


main()

'''

global final_score

def main():
    final_grade = average_score()
    grader(final_grade)


def average_score():
    test_1 = int(input('What was your score for test one?: '))
    test_2 = int(input('What was your score for test two?: '))
    test_3 = int(input('What was your score for test three?: '))
    test_4 = int(input('What was your score for test four?: '))
    test_5 = int(input('What was your score for test five?: '))
    final_score = (test_1 + test_2 + test_3 + test_4 + test_5)
    print(final_score/5)
    return (final_score/5)
def grader(final_score):
    if final_score == 100:
        print('you got an A+, Congrats')
    elif final_score >= 90 and final_score < 100:
        print('you just got an A')
    elif final_score >= 80 and final_score < 90:
        print('you got a B')
    elif final_score >= 70 and final_score < 80:
        print(' You got a C')
    elif final_score >= 60 and final_score < 70:
        print('You got a D')
    else:
        print('you got an F')

main()



