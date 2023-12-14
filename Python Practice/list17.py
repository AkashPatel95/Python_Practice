#Python program to print positive numbers in a list

test_list=[12, -7, 5, 64, -14]

new_list=[]

for i in test_list:
    if i>0:
        new_list.append(i)

print(new_list)