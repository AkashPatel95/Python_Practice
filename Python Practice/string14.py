#Python | Maximum frequency character in String
test_string=input("Enter a string:")

freq_dict={}

for i in test_string:
    if i not in freq_dict:
        freq_dict[i]=1
    else:
        freq_dict[i]+=1

max_value=max(freq_dict.values())

for key,value in freq_dict.items():
    if value==max_value:
        max_freq_char=key
        break
print("Maximum frequency value: ",max_freq_char)