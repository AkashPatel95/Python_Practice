#Python – Replace duplicate Occurrence in String

input_string=input("Enter a string:")

result_string=""

for i in input_string:
    if i not in result_string:
        result_string+=i

print(result_string)