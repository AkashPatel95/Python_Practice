#Write a Python function to check whether a number falls within a given range.

def num_in_givenrange(num):
    start=3
    end=9
    if num>=3 and num<=9:
        print(num,"in given range")
    else:
        print(num,"not in given range")

num=int(input("Enter a number:"))
num_in_givenrange(num)