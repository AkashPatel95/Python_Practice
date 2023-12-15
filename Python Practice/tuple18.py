#Python – Assign Frequency to Tuples

test_list=[(6, 5, 8), (2, 7), (6, 5, 8), (9, ), (2, 7)]

freq_list=[]

for ele in set(test_list):
    freq_list.append((*ele,test_list.count(ele)))

print(freq_list)

