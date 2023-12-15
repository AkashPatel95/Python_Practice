#Python – Maximum and Minimum K elements in Tuple

test_tuple=(3, 7, 1, 18, 9)
k=2

sorted_tuple=sorted(test_tuple)
print(sorted_tuple[:k]+sorted_tuple[-1:-k-1:-1])