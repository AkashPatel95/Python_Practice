'''
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''

def multiplication(test_list):
    multiply=1
    for i in test_list:
        multiply*=i
    print(multiply)

multiplication([8, 2, 3, -1, 7])