'''Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd'''
from itertools import product
test_dict={'1':['a','b'], '2':['c','d']}

combinations=list(product(*test_dict.values()))

for combination in combinations:
    print("".join(combination))


