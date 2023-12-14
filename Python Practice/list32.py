#Python – Extract elements with Frequency greater than K
from collections import Counter
test_list=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]

k=3
new_list=Counter(test_list)

result=[]

for key,value in new_list.items():
    if value>k:
        result.append(key)

print(result)
