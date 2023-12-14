#Remove multiple elements from a list in Python

test_list=[12, 15, 3, 10]

remove=[12, 3]

new_list=[]

for i in test_list:
    if i not in remove:
        new_list.append(i)

print(new_list)