#Python – Modulo of tuple elements
test_tuple1=(10, 4, 5, 6)
test_tuple2=(5,6,7,5)

new_list=[]

for i in range(0,len(test_tuple1)):
    for j in range(i,i+1):
        new_list.append(test_tuple1[i]%test_tuple2[j])

print(tuple(new_list))
