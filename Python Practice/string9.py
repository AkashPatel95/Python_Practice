#Python program to print even length words in a string
test_str=input("Enter a string:")

new_str=test_str.split(" ")

words=[]

for i in new_str:
    if len(i)%2==0:
        words.append(i)

print(words)