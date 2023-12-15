#Python – Adding Tuple to List and vice – versa
test_list=[5, 6, 7]
test_tuple=(5, 6, 7)

add_to_list=(8,9)
add_to_tuple=[8,9]

new_list=test_list+list(add_to_list)
new_tuple=test_tuple+tuple(add_to_tuple)

print(new_list)
print(new_tuple)