#Python | Sum of number digits in List

test_list=[12, 67, 98, 34]

new_list=[]

for i in test_list:
    str_value=str(i)
    total=0
    for j in str_value:
        total+=int(j)
    new_list.append(total)

print(new_list)