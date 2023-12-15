'''Tuple Deletion:**
    - **Data:** `(1, 2, 3)`, `2`
    - **Question:** Delete the element `2` from the tuple.
'''

test_tuple=(1, 2, 3)
ele=2
new_list=[]

for i in test_tuple:
    if i!=ele:
        new_list.append(i)

print(tuple(new_list))