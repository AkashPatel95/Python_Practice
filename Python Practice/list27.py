#Python program to find Cumulative sum of a list

test_list=[10, 20, 30, 40, 50]

new_list=[]

total=0

for i in test_list:
    total+=i
    new_list.append(total)

print(new_list)