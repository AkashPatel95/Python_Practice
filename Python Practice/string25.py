#Python – Find all duplicate characters in string

test_string=input("Enter a string:")

final_list=[]

for i in range(0,len(test_string)):
    for j in range(i+1,len(test_string)):
        if test_string[i]==test_string[j]:
            if test_string[i] not in final_list:
                final_list.append(test_string[i])

print(final_list)
    