#Python | Program to print duplicates from a list of integers

test_list=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

new_list=[]

for i in test_list:
    if test_list.count(i)>1:
        if i not in new_list:
            new_list.append(i)

print(new_list)