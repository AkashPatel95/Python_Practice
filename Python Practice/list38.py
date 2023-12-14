#Remove all the occurrences of an element from a list in Python

test_list=[1, 1, 2, 3, 4, 5, 1, 2]
remove_item=1
new_list=[]

for i in test_list:
    if i!=remove_item:
        new_list.append(i)

print(new_list)
