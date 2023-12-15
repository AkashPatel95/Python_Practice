#Python – Remove Tuples from the List having every element as None

test_list=[(None, 2), (None, None), (3, 4), (12, 3), (None, )]

new_list=[]

for i in test_list:
    count=0
    for j in i:
        if j==None:
            count+=1
    if count!=2:
        new_list.append(i)

print(new_list)
