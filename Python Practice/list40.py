#Python – Replace index elements with elements in Other List

test_list1=['Gfg', 'is', 'best']
test_list2=[0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

new_list=[]
for i in test_list2:
    new_list.append(test_list1[i])

print(new_list)