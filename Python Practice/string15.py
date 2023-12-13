#Program to check if a string contains any special character
test_string=input("Enter a string:")

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '~', '`']

spec_char_exist=False

for i in special_characters:
    if i  in test_string:
        spec_char_exist=True
        break

if spec_char_exist:
    print("Special Character Exist")
else:
    print("Special Character Does Not Exist")
