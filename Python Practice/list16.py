#Python program to print all odd numbers in a range

start=int(input("Enter a number from where you want to start:"))
end=int(input("Enter a number at where you want to end:"))

new_list=[]

for i in range(start,end+1):
    if i%2!=0:
        new_list.append(i)

print(new_list)