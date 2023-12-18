'''Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y'''

test_dict1={'key1': 1, 'key2': 3, 'key3': 2}
test_dict2={'key1': 1, 'key2': 2}

for key,value in test_dict1.items():
    if key in test_dict2.keys() and value==test_dict2[key]:
        print(key,"is present")
