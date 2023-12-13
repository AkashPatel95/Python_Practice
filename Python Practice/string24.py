#Python | Permutation of a given string using inbuilt function
from itertools import permutations

test_string="abc"

permutation_string=permutations(test_string,3)

for perm in permutation_string:
    print("".join(perm))