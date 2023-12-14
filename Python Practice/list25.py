#Python | Remove empty tuples from a list

test_list=[(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]

new_list=[]

for i in test_list:
    if i!=():
        new_list.append(i)

print(new_list)