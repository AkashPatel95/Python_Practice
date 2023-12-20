'''
Write a Python function that takes a number as a parameter 
and checks whether the number is prime or not.
'''
def prime_or_not(num):
    if num>1:
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            print(num,"is prime")
        else:
            print(num,"is not prime")
    else:
        (num,"is not prime")

num=int(input("Enter a number:"))
prime_or_not(num)