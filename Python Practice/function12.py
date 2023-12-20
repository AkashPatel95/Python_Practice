#Write a Python function that checks whether a passed string is a palindrome or not.

def palindrome_or_not(string):
    if string==string[-1::-1]:
        print("String is palindrome")
    else:
        print("String is not palindrome")


string=input("Enter a string:")
palindrome_or_not(string)