'''Write a Python program to combine values in a list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})'''

test_list=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

new_dict={}

for i in test_list:
    item_key=i['item']
    amount_value=i['amount']

    if item_key not in new_dict:
        new_dict[item_key]=amount_value
    else:
        new_dict[item_key]+=amount_value

print(new_dict)