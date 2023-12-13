#Python program to split and join a string

input_string=input("Enter a string:")

split_string=input_string.split(" ")
join_string="-".join(split_string)
print(join_string)