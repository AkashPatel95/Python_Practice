#Write a Python program to multiply all the items in a dictionary.

test_dict={'data1': 100, 'data2': -54, 'data3': 247}

multiply=1

for i in test_dict.values():
    multiply*=i

print(multiply)