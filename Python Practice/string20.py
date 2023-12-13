#Python | Check if a given string is binary string or not

input_string=input("enter a string:")

check=set(input_string)
binary={'0','1'}

if check==binary or check=={'0'} or check=={'1'}:
    print("Binary string")
else:
    print("Non Binary String")