#Python – Words Frequency in String Shorthands
from collections import Counter
str1=input("Enter a string:")

new_list=str1.split(" ")
final_result=Counter(new_list)
print(final_result)

