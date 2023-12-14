#Python program to print even numbers in a list

test_list=[2, 7, 5, 64, 14]

new_list=[]

for i in test_list:
    if i%2==0:
        new_list.append(i)

print(new_list)