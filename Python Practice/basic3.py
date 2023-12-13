#Python Program for factorial of a number

num=int(input("Enter a number to get factorial:"))

fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial:",fact)