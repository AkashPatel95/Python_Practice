#Python Program to Accept the Strings Which Contains all Vowels
test_str=input("Enter a string:")

new_str=set(test_str.lower())

vowels=['a','e','i','o','u']
count=0
for i in vowels:
    if i in new_str:
        count+=1

if count==5:
    print("String accepted")
else:
    print("String not accepted")
