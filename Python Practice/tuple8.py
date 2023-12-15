#Python | Update each element in tuple list

test_tuple=[(1, 3, 4), (2, 4, 6), (3, 8, 1)]
add=4

new_list=[]

for i in test_tuple:
    list1=[]
    for j in i:
        list1.append(j+add)
    new_list.append(tuple(list1))

print(new_list)