#Create a list of tuples from given list having number and its cube in each tuple
test_list=[1, 2, 3]

new_list=[]

for i in test_list:
    new_list.append((i,i*i*i))

print(new_list)