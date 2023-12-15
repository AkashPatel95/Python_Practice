# Python – Records with Value at K index

test_list=[(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]

ele=3
k=1

new_list=[]

for eleme in test_list:
    if eleme[k]==ele:
        new_list.append(eleme)

print(new_list)