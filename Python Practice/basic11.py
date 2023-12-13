'''Python Program for How to check if a given number is Fibonacci number?'''

num=int(input("Enter a number:"))

new_list=[0,1]
a,b=0,1

for i in range(2,num):
    temp=a+b
    a=b
    b=temp
    new_list.append(temp)

if num in new_list:
    print("Fibonacci Number")
else:
    print("Non Fibonacci Number")