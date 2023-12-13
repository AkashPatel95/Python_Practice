#Python program for removing i-th character from a string
test_string=input("Enter a string:")

i=int(input("Enter a index number to remove from string:"))

if i!=0:
    new_string=test_string[:i]+test_string[i+1:]
else:
    new_string=test_string[1:]

print(new_string)