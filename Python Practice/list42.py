#Python Program to Sort the list according to the column using lambda

test_list=[['java', 1995], ['c++', 1983],
             ['python', 1989]]

sorted_list=sorted(test_list,key=lambda x:x[1])
print(sorted_list)