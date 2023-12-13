#Python – Least Frequent Character in String
test_string=input("Enter a string:")

freq_dict={}
for i in test_string:
    if i not in freq_dict:
        freq_dict[i]=1
    else:
        freq_dict[i]+=1

min_value=min(freq_dict.values())

for key,value in freq_dict.items():
    if value==min_value:
        least_freq_char=key
        break
print("Least frequent character:",least_freq_char)
