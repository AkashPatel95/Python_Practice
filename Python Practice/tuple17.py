#Python – Filter Range Length Tuples

test_list=[(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

new_list=[]

h,j=2,3

for i in test_list:
    if len(i)>=h and len(i)<=j:
        new_list.append(i)

print(new_list)