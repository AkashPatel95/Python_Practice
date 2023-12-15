#Python – Elements frequency in Tuple

test_tuple=(4, 5, 4, 5, 6, 6, 5)

dict1={}

for i in test_tuple:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1

print(dict1)