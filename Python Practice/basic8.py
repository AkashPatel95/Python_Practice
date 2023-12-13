#Python program to print all Prime numbers in an Interval
starting_range=int(input("Enter a starting range:"))
ending_range=int(input("Enter ending range:"))

new_list=[]

for i in range(starting_range,ending_range+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        new_list.append(i)

print(new_list)