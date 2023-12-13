#Python program to check whether the string is Symmetrical or Palindrome
str1=input("enter a string:")

str2=str1[-1::-1]
if str1==str2:
    print("String is palindrome")
else:
    print("String is not palindrome")

if len(str1)%2==0:
    if str1[:len(str1)//2]==str1[len(str1)//2:]:
        print("String is symmetrical")
    else:
        print("String is not symmetrical")
else:
    print("String is not symmetrical")