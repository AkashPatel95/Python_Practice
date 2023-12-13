#Python Program for compound interest
p=int(input("Enter an amount:"))
r=float(input("Enter a rate of interest:"))
t=int(input("Enter a time:"))

a=p*pow(1+(r/100),t)

compound_interest=a-p
print(compound_interest)