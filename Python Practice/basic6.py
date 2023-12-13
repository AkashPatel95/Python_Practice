#Python Program to check Armstrong Number

num=int(input("Enter a number to check if is armstrong or not:"))
temp=num
total=0
while num!=0:
    nume=num%10
    total=nume*nume*nume+total
    num=num//10
if temp==total:
    print("Armstrong")
else:
    print("Non Armstrong")