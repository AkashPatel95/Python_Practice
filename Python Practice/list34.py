#Python program to check if the list contains three consecutive common numbers in Python

test_list=[1, 1, 1, 64, 23, 64, 22, 22, 22]

new_list=[]

for i in range(0,len(test_list)-2):
    if test_list[i]==test_list[i+1]==test_list[i+2]:
        if test_list[i] not in new_list:
            new_list.append(test_list[i])

print(new_list)