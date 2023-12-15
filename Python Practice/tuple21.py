'''Tuple Intersection:**
   - **Data:** `(1, 2, 3)`, `(2, 3, 4)`
   - **Question:** Find the common elements between two tuples.
'''
test_tpl1=(1, 2, 3)
test_tpl2=(2, 3, 4)

for i in test_tpl1:
    if i in test_tpl2:
        print(i)


