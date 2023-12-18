#Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

test_dict={'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

sorted_dict=dict(sorted(test_dict.items(),key=lambda x:x[1],reverse=True))

count=0
for key,value in sorted_dict.items():
    if count!=3:
        print(key)
        count+=1
    else:
        break

