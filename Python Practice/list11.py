#Python program to find second largest number in a list
test_list=[10, 20, 4]

new_list=sorted(test_list,reverse=True)
print(new_list[1])