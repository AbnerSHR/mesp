import sys


def print_how_to_use_it():
    print('You should provide 2 arguments to run this project properly:')
    print('\tFirst: a list of integers separated by comma without spaces')
    print('\tSecond: an integer to be used as base to find pairs from the list that sum to its value')
    print('\tExample: python mesp.py 1,9,5,0,20,-4,12,16,7 12')
    exit(0)


def check_command_line_parameters():
    # print('\n', '*'*80, '\n', sys.argv, '\n',  '*'*80, '\n', )
    if len(sys.argv) != 3:
        print_how_to_use_it()
    return check_sum_parameters(sys.argv[1], sys.argv[2])


def check_sum_parameters(par1_list: str, par2_sum: str):
    alist = []
    asum = 0
    try:
        asum = int(par2_sum)
    except ValueError as e:
        print(f'{par2_sum} is NOT a valid parameter')
        print_how_to_use_it()

    try:
        alist = list(int(x) for x in par1_list.split(','))
    except ValueError as e:
        print(f'ValueError: {par1_list} is NOT a valid parameter')
        print_how_to_use_it()

    return check_sum(alist, asum)


def check_sum(alist: list, asum: int):

    if len(alist) < 2:
        # print('No pair found.')
        return []

    alist.sort()

    if (alist[0] + alist[1]) > asum:
        # print('No pair found.')
        return []
    prior = alist[-2:][1]
    if alist[-1] + prior < asum:
        # print('No pair found.')
        return []

    asums = []
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if alist[i] + alist[j] == asum:
                asums.append(f'{alist[i]},{alist[j]}')

    return asums


if __name__ == '__main__':
    result = check_command_line_parameters()
    for r in result:
        print(r)


