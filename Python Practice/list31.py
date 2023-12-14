#Python – List product excluding duplicates

test_list=[1, 3, 5, 6, 3, 5, 6, 1]

test_list_set=set(test_list)
new_list=list(test_list_set)
multiply=1
for i in new_list:
    multiply*=i

print(multiply)