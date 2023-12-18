#Write a Python program to remove a key from a dictionary.

test_dict={'a': 1, 'b': 2, 'c': 3, 'd': 4}

key_remove='a'

if key_remove in test_dict:
    test_dict.pop(key_remove)

print(test_dict)