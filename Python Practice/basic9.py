#Python program to check whether a number is Prime or not

num=int(input("Enter a number:"))

count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Non Prime Number")