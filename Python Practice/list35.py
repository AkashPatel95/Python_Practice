#Python program to find the Strongest Neighbour

test_list=[1,2,2,3,4,5]

new_list=[]

for i in range(0,len(test_list)-1):
    if test_list[i]<=test_list[i+1]:
        new_list.append(test_list[i+1])

print(new_list)


