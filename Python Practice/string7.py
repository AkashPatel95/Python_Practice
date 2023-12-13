#Python – Convert Snake case to Pascal case

input_str=input("Enter a string:")

words=input_str.split("_")
new_str=""
for word in words:
    new_str+=word.capitalize()

print(new_str)