#Python program to find uncommon words from two Strings

test_string1=input("Enter a string:")
test_string2=input("Enter a string:")

test_string1_list1=test_string1.split(" ")
test_string2_list2=test_string2.split(" ")

final_list=[]

for word in test_string1_list1:
    if word not in test_string2_list2:
        final_list.append(word)


for word in test_string2_list2:
    if word not in test_string1_list1:
        final_list.append(word)

print(final_list)