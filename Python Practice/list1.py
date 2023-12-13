#Python program to interchange first and last elements in a list

test_list=[12, 35, 9, 56, 24]

new_list=[test_list[-1]]+test_list[1:len(test_list)-1]+[test_list[0]]
print(new_list)