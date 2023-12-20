'''
Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def count_upper_lower_case(string):
    upper_count=0
    lower_count=0
    for i in string:
        if i.isupper():
            upper_count+=1
        else:
            lower_count+=1
    return upper_count,lower_count


upper_count,lower_count=count_upper_lower_case('The quick Brow Fox')
print("Upper case:",upper_count)
print("Lower case:",lower_count)