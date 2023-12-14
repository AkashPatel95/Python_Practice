#Python program to find N largest elements from a list
test_list=[4, 5, 1, 2, 9]
n=2

new_list=sorted(test_list,reverse=True)

print(new_list[:n])