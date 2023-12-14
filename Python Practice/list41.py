#Python – Retain records with N occurrences of K

test_list=[(4, 5, 5, 4), (5, 4, 3)]
k,n=5,2

new_list=[]

for i in test_list:
    count=0
    for j in i:
        if j==k:
            count+=1
    if count==n:
        new_list.append(i)

print(new_list)