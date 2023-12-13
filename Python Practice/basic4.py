#Python Program for simple interest

p=int(input("Enter a principle amount:"))
r=float(input("Enter rate of interest:"))
t=int(input("Enter a time:"))

simple_interest=(p*r*t)/100
print(simple_interest)