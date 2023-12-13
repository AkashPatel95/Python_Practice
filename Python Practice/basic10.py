#Python Program for n-th Fibonacci number
num=int(input("Enter a range to get fibonacci number upto:"))

a=0
b=1
print(a)
print(b)
for i in range(2,num):
    temp=a+b
    a=b
    b=temp
    print(temp)