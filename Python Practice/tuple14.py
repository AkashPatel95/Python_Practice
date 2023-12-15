#Python program to sort a list of tuples by second Item

test_list=[('for', 24), ('Geeks', 8), ('Geeks', 30)]

new_list=sorted(test_list,key=lambda x:x[1])
print(new_list)