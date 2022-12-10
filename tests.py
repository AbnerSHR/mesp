import unittest
import os
import sys
import mesp as mesp


sub_tests_from_file = False
sub_tests = 0
sub_tests_passed = 0


def compare_lists(list1, list2):
    if len(list2) > len(list1):
        # print('list1:', list1, 'list2:', list2)
        return False
    for pair in list2:
        if pair not in list1:
            if pair.__contains__(','):
                pair = pair.split(',')[1] + ',' + pair.split(',')[0]
                if pair not in list1:
                    # print(f'pair {pair} not in list1')
                    return False
            else:
                # print('pair does not contains a comma')
                return False
    return True


class TestChallenge(unittest.TestCase):

    def test_check_command_line_parameters_01(self):
        while len(sys.argv) > 1:
            sys.argv.pop()
        sys.argv.append('1,9,5,0,20,-4,12,16,7')
        sys.argv.append('12')
        atest = mesp.check_command_line_parameters()
        # self.asserttEqual(atest, ['-4,16', '0,12', '5,7'])
        self.assertTrue(compare_lists(atest, ['-4,16', '0,12', '5,7']))

    def test_check_sum_parameters_01(self):
        atest = mesp.check_sum_parameters('1,9,5,0,20,-4,12,16,7', '12')
        # self.assertEqual(atest, ['-4,16', '0,12', '5,7'])
        self.assertTrue(compare_lists(atest, ['-4,16', '0,12', '5,7']))

    def test_check_sum_parameters_02_from_file(self):
        fname = 'tests.txt'
        if not os.path.exists(fname):
            return
        file = open(fname, mode='r')
        lines = file.readlines()
        file.close()
        global sub_tests_from_file
        sub_tests_from_file = True
        for iline in range(len(lines)):
            line = lines[iline]
            # print('SubTest:', iline, end=' ')
            global sub_tests
            global sub_tests_passed
            sub_tests += 1
            with self.subTest(msg=line, line=line):
                pars = line.split(' ')
                if len(pars) == 2:
                    atest = mesp.check_sum_parameters(pars[0], pars[1])
                    self.assertEqual(atest, [])
                    if not atest:
                        sub_tests_passed += 1
                    # print('passed') if atest == [] else print('NO PASSED')
                if len(pars) == 3:
                    arg3 = pars[2].replace('\n', '').split(',')
                    aresult = []
                    if arg3[0] != '':
                        for i in range(0, len(arg3), 2):
                            aresult.append(f'{arg3[i]},{arg3[i+1]}')
                    atest = mesp.check_sum_parameters(pars[0], pars[1])
                    result = compare_lists(atest, aresult)
                    self.assertTrue(result)
                    if result:
                        sub_tests_passed += 1
                    # print('passed') if result else print('NO PASSED')

    def test_check_sum_01(self):
        atest = mesp.check_sum([1, 9, 5, 0, 20, -4, 12, 16, 7], 12)
        # self.assertEqual(atest, ['-4,16', '0,12', '5,7'])
        self.assertTrue(compare_lists(atest, ['-4,16', '0,12', '5,7']))


test_result = unittest.main(argv=[''], verbosity=1, exit=False)

print('Tests run:', test_result.result.testsRun)
print('Tests failures:', len(test_result.result.failures))
print('Tests errors:', len(test_result.result.errors))
print('Tests passed:', test_result.result.testsRun
      - len(test_result.result.failures)
      - len(test_result.result.errors))
if sub_tests_from_file:
    print('Sub tests from file:', sub_tests)
    print('Sub tests from file fails:', sub_tests - sub_tests_passed)
    print('Sub tests from file passed:', sub_tests_passed)
