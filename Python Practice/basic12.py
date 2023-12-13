#Python Program for nth multiple of a number in Fibonacci Series
k=int(input("Enter k:"))
n=int(input("Enter n:"))

num=pow(n,k)
new_list=[0,1]
a,b=0,1
for i in range(2,num+1):
    temp=a+b
    a=b
    b=temp
    new_list.append(temp)

print(new_list[num])