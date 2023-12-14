#Python – Remove empty List from List

test_list=[5, 6, [], 3, [], [], 9]

new_list=[]

for i in test_list:
    if i!=[]:
        new_list.append(i)

print(new_list)