import sys
# import big_o


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


def check_sum(alist: list, asum: int = 12):  # asum default to 12 to big-o test

    # Check the length of the list
    if len(alist) < 2:
        # print('No pair found.')
        return []

    asums = []  # to save results

    # Let's check the list from the last item
    for i in range(len(alist)-1, -1, -1):
        anum = alist[i]
        del alist[i]  # remove de item from the list

        difference = asum - anum

        if difference == asum // 2:
            # You can assume that there aren't
            # any repeat values in the list.
            continue
        if difference in alist:
            # There is a match, so put it in the results list
            asums.append(f'{anum},{difference}')

    return asums


if __name__ == '__main__':
    result = check_command_line_parameters()
    for r in result:
        print(r)

    # A single big-O test (must uncomment the 2nd line of code) and install the package [pip install big-o]
    # ig = lambda n: big_o.datagen.integers(n, -10000, 10000)
    # best, others = big_o.big_o(check_sum, ig, n_repeats=100)
    # print(best)
