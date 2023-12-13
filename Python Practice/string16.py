#Generating random strings until a given string is generated

import random
import string

test_string=input("Enter a string:")
generated_string=""
attempts=0

while generated_string!=test_string:
    generated_string=""
    for i in range(0,len(test_string)):
        generated_string+=random.choice(string.ascii_letters)

    attempts+=1

print("Matching string is generated after",attempts,"attempts")