#Remove all duplicates from a given string in Python
test_string=input("Enter a string:")
new_str=""
for i in test_string:
    if i not in new_str:
        new_str+=i

print(new_str)