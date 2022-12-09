## Mach Eight Sample Project

Please see the [README_entry_level.md](README_entry_level.md) file to check the requirements for this project.

Language used:
```
Python 3.9.6
```
To run it:
```
python mesp.py [a comma separated list of integers] [the target integer]
```
Example:
```
python mesp.py 1,9,5,0,20,-4,12,16,7 12
```
Output:
```
-4,16
0,12
5,7
```

### IMPORTANT:
#### The order of each line and the order of each pair in each line of the result may be different from the expected one, but always the sum of the elements in each line must be equal to the target integer.

#### NOTE:
 If the parameters are not provided, a message will appear with instructions on how to run the test, like this:
```
You should provide 2 arguments to run this project properly:
        First: a list of integers separated by comma without spaces
        Second: an integer to be used as base to find pairs from the list that sum to its value
        Example: python mesp.py 1,9,5,0,20,-4,12,16,7 12
```
## Unit tests:
To run unit test, just use the following command:
```
python tests.py
```
The [tests.txt](tests.txt) file contains 100 lines to pass as parameters to test.
- Each line contains 3 parameters separated by a single space
  1. A comma separated list of integers
  2. The target integer: the sum to search for.
  3. The expected result as a comma-separated list of integers, where every two elements correspond to a sum pair.
### How to generate the tests.txt file (aditional)
- Note that this program is not part of the chanllenge.
- The python program [create_tests_file.py](create_tests_file.py) generates a new [tests.txt](tests.txt) file with several aditional tests cases.  You can change then initial variables to create more or less tests. 
To run it, type the command:
  ```
  python create_tests_file.py
  ```
  Then, run [Unit tests](#unit-tests-).