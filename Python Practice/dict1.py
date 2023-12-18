#Write a Python script to sort (ascending and descending) a dictionary by value.

test_dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

ascending_sort=sorted(test_dict.items(),key=lambda x:x[1])

descending_sort=sorted(test_dict.items(),key=lambda x:x[1],reverse=True)

print(ascending_sort)
print(descending_sort)