#Python – Sort Tuples by Total digits

test_list=[(3, 4, 6, 723), (1, 2), (134, 234, 34)]

new_list=sorted(test_list,key=lambda tup:sum([len(str(ele)) for ele in tup]))

print(new_list)

