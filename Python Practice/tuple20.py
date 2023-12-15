#Python | Test if tuple is distinct

test_tuple=(1, 4, 5, 6, 1, 4)

is_distinct=len(set(test_tuple))==len(test_tuple)

if is_distinct:
    print("True")
else:
    print("False")