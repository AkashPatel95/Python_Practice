#Write a Python script to merge two Python dictionaries.

dict1={'a': 100, 'b': 200}
dict2={'x': 300, 'y': 200}

new_dict={}

for i in dict1,dict2:
    new_dict.update(i)

print(new_dict)