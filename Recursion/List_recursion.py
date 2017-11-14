def main():
    numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    my_sum = ranger(numbers, 1, 9)

    print('The Sum of items 1 through 9 is:', my_sum)

def ranger(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + ranger(num_list, start + 1, end)


main()
