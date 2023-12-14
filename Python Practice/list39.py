#Python – Remove Consecutive K element records

test_list=[(4, 5), (5, 6), (1, 3), (0, 0)]
k=0

new_list=[]

for i in test_list:
    if sum(i)!=0:
        new_list.append(i)

print(new_list)