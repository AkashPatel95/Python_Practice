'''
Write a Python function to create and print a list 
where the values are the squares of numbers between 1 and 30 (both included).
'''

def create_list():
    new_list=[]
    for i in range(1,31):
        new_list.append(i*i)

    return new_list


print(create_list())