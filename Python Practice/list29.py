#Sort the values of first list using second list in Python

test_list=["a", "b", "c", "d", "e", "f", "g", "h", "i"]

dummy=[0,1,1,0,1,2,2,0,1]

new_list1=[]
new_list2=[]
new_list3=[]
for i in range(0,len(dummy)):
    for j in range(i,i+1):
        if dummy[i]==0:
            new_list1.append(test_list[j])
        elif dummy[i]==1:
            new_list2.append(test_list[j])
        elif dummy[i]==2:
            new_list3.append(test_list[j])

new_list=new_list1+new_list2+new_list3
print(new_list)

