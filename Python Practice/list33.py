#Python – Test if List contains elements in Range
test_list=[4, 5, 6, 7, 3, 9]
j,k=3,10

is_contain=False
for i in test_list:
    if i>=j and i<=k:
        is_contain=True
    else:
        is_contain=False
        break

if is_contain:
    print("True")
else:
    print("False")

