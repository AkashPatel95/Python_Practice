'''
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''

def check_even_or_not(test_list):
    new_list=[]
    for i in test_list:
        if i%2==0:
            new_list.append(i)

    return new_list


print(check_even_or_not([1, 2, 3, 4, 5, 6, 7, 8, 9]))