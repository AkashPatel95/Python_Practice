#Python | Count occurrences of an element in a list

test_list=[15, 6, 7, 10, 12, 20, 10, 28, 10]
n=10

count=0
for i in test_list:
    if i==n:
        count+=1

print(count)