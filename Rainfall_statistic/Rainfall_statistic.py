"""
so this program will give the yearly average of rainfall
"""


def main():
    monthly()


def monthly():
    global total_avg
    averages = []
    yearly = 0

    months = ['january', 'february', 'march', 'april', 'june', 'july', 'august', 'september', 'october', 'november',
              'december']
    for m in range(len(months)):
        a = int(input('How much did it rain for month: '))
        averages.append(a)

    for n in range(len(averages)):
        yearly += averages[n]
        total_avg = yearly/12
    print(format(total_avg, ',.2f'))
    print('The lowest number in the list is:', format(min(averages), ',.2f'))
    print('The highest number in the list is:', format(max(averages), ',.2f'))


main()
