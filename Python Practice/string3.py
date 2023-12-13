#Reverse words in a given String in Python
str1=input("Enter a string:")

new_list=str1.split(" ")
reverse_list=new_list[-1::-1]
new_str=" ".join(reverse_list)
print(new_str)