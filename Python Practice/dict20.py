'''Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3'''

test_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

sorted_dict=dict(sorted(test_dict.items(),key=lambda x:x[1],reverse=True))

count=0

for key,value in sorted_dict.items():
    if count!=3:
        print(key,":",value)
        count+=1
    else:
        break