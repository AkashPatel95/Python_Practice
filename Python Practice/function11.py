#Write a Python function to check whether a number is "Perfect" or not.

def perfect_or_not(num):
    divisor_sum=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            divisor_sum+=i

    if divisor_sum==num:
        print("perfect number")
    else:
        print("non perfect number")


num=int(input("Enter a number:"))
perfect_or_not(num)