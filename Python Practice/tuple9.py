#Python | Multiply Adjacent elements

test_tuple=(1, 5, 7, 8, 10)

final_list=[]

for i in range(0,len(test_tuple)-1):
    final_list.append(test_tuple[i]*test_tuple[i+1])

print(tuple(final_list))