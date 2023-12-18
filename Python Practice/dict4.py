#Write a Python script to check whether a given key already exists in a dictionary.

test_dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key=5

if key in test_dict:
    print("True")
else:
    print("False")