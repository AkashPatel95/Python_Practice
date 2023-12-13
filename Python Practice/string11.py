#Python | Count the Number of matching characters in a pair of string
test_str=input("Enter a string:")
str2="defghia"
new_str=set(test_str)
new_str2=set(str2)

count=0
for i in new_str:
    if i in new_str2:
        count+=1

print(count)