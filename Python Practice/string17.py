#Find words which are greater than given length k
test_string=input("Enter a string:")

k=4

new_list=test_string.split(" ")
new_string=""

for word in new_list:
    if len(word)>k:
        new_string+=word+" "

print(new_string)
