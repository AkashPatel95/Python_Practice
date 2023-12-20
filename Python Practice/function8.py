'''
Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_element(test_list):
    test_set=set(test_list)
    return list(test_set)


print(unique_element([1,2,3,3,3,3,4,5]))