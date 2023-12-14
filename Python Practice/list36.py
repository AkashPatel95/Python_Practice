#Python Program to print all Possible Combinations from the three Digits
from itertools import permutations
test_list=[1, 2, 3]

new_list=permutations(test_list)

for i in new_list:
    print(i)