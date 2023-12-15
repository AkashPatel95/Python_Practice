#Python – Remove Tuples of Length K

test_list=[(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

k=2

result=[]

for i in test_list:
    if len(i)!=k:
        result.append(i)

print(result)