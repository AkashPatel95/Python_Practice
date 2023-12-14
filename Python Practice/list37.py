#Python program to get all unique combinations of two Lists
from itertools import product
list1=["a","b"]
list2=[1,2]

new_list=product(list1,list2)
for i in new_list:
    print(i)