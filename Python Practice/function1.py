#Write a Python function to find the maximum of three numbers.

def max_of_three(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"is maximum")
    elif num2>num3:
        print(num2,"is maximum")
    else:
        print(num3,"is maximum")

max_of_three(5,6,7)