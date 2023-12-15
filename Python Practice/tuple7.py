#Python – Row-wise element Addition in Tuple Matrix

test_list=[[('Gfg', 3)], [('best', 1)]]

add_ele=[1, 2] 

new_list=[]

for sublist,ele in zip(test_list,add_ele):
    updated_sublist=[]
    for tpl in sublist:
        updated_sublist.append((*tpl,ele))
    new_list.append(updated_sublist)

print(new_list)