#Python program to swap two elements in a list
test_list=[23, 65, 19, 90]
pos1=1
pos2=3

new_list=test_list[0:pos1]+[test_list[pos2]]+test_list[2:pos2]+[test_list[pos1]]
print(new_list)