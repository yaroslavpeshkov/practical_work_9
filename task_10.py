def amount(number_n, k):
    '''
    The function counts amount of possible ladders.
    :param number_n: amount of blocks
    :param k: amount of blocks in last row
    :return: amount of possible ladders
    '''
    if number_n == 0:
        return 1
    count = 0
    for i in range(k + 1, number_n + 1):
        count += amount(number_n - i, i)
    return count


def main():
    '''
    Main function.
    :return: amount of possible ladders
    '''
    number_n = int(input())
    k = 0
    return amount(number_n, k)


print(main())
