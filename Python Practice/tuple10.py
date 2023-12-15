#Python – Join Tuples if similar initial element

test_list=[(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

test_list=sorted(test_list,key=lambda x:x[0])

final_list=[]

current_tuple=test_list[0]

for ele in test_list[1:]:
    if current_tuple[0]==ele[0]:
        current_tuple=(*current_tuple,*ele[1:])
    else:
        final_list.append(current_tuple)
        current_tuple=ele

final_list.append(current_tuple)

print(final_list)


